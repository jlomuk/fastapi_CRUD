from typing import List, Optional

from fastapi import Depends
from fastapi.routing import APIRouter

from schemas.user_schemas import User, UserCreate
from services.user_services import UserService

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/', response_model=List[User])
def get_list_users(active: Optional[bool] = None, user_service: UserService = Depends()):
    return user_service.get_users_list(active)


@router.get('/{user_id}', response_model=User)
def get_user(user_id: int, user_service: UserService = Depends()):
    return user_service.get_user(user_id)


@router.post('/createuser', response_model=User)
def create_user(user: UserCreate, user_service: UserService = Depends()):
    return user_service.create_user(user)