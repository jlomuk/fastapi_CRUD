import datetime
import bcrypt

from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from starlette import status
from models.user import User as UserModel
from schemas.user_schemas import User, Token
from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def check_and_return_user_to_token(token: str = Depends(oauth2_scheme)) -> User:
    return AuthMixin.validate_token(token)


class AuthMixin:

    def get_hashed_password(self, plain_password):
        hash = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        return hash.decode()

    def check_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )

    def create_token_jwt(self, db_user: UserModel) -> Token:
        user_valid = User.from_orm(db_user)
        data_token = {
            "sub": str(user_valid.id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(
                minutes=settings.access_token_expire_minutes
            ),
            "user": user_valid.dict()
        }
        token = jwt.encode(data_token, settings.secret_key, settings.algorithm)
        return Token(access_token=token)

    @staticmethod
    def validate_token(token: str) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            data_token = jwt.decode(token=token, key=settings.secret_key, algorithms=settings.algorithm)
        except JWTError as e:
            raise credentials_exception
        user_dict = data_token.get('user')
        try:
            user = User.parse_obj(user_dict)
        except ValidationError:
            raise credentials_exception
        return user
