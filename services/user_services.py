from typing import List

from fastapi import Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session, Query

from core.database import get_db
from models.user import User
from schemas.user_schemas import UserCreate


class UserService:
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
        print(type(user))
        return user

    def create_user(self, user: UserCreate) -> User:
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        return db_user

