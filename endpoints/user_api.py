from typing import List, Optional

from fastapi import Depends
from fastapi import Response
from fastapi.routing import APIRouter
from starlette import status

from schemas.user_schemas import User, UserCreate, UserUpdate
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


@router.put('/{user_id}/update', response_model=User)
def update_user(
        user_id: int,
        update_data: UserUpdate,
        user_service: UserService = Depends()
):
    return user_service.update_user(user_id, update_data)


@router.delete('/{user_id}/delete')
def delete_user(user_id: int, user_service: UserService = Depends()):
    user_service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
