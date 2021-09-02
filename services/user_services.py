from fastapi import Depends, HTTPException
from starlette import status

from core.database import Session
from models.user import User


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


class UserService:

    def __init__(self, session: Session = next(get_db())):
        self.db = session
        self.user = User

    def _get_users_query(self):
        query = self.db.query(User)
        return query

    def get_users_list(self):
        list_users = self._get_users_query().all()
        return list_users

    def get_user(self, user_id):
        user = self._get_users_query().filter(self.user.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exists')
        return user
