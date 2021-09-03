from typing import List

from fastapi import Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session, Query

from core.database import get_db
from models.user import User
from schemas.user_schemas import UserCreate, UserUpdate
from services.mixins import PasswordHashMixin


class UserService(PasswordHashMixin):
    """Класс содержит CRUD логику для User модели"""

    def __init__(self, session: Session = Depends(get_db)) -> None:
        self.db = session

    def _get_users_query(self) -> Query:
        query = self.db.query(User)
        return query

    def get_users_list(self, active: bool) -> List[User]:
        query = self._get_users_query()
        if active is not None:
            query = query.filter(User.is_active == active)
        list_users = query.all()
        return list_users

    def get_user(self, user_id: int) -> User:
        user = self._get_users_query().filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exists')
        return user

    def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.dict())
        db_user.password = self.get_hashed_password(user.password)
        self.db.add(db_user)
        self.db.commit()
        return db_user

    def update_user(self, user_id: int, update_data: UserUpdate) -> User:
        db_user = self.get_user(user_id)
        for key, value in update_data.dict().items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> None:
        db_user = self.get_user(user_id=user_id)
        self.db.delete(db_user)
        self.db.commit()
