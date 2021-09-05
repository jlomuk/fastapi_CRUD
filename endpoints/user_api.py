from typing import List, Optional

from fastapi import Depends, HTTPException
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
    return user_service.get_user_by_id(user_id)


@router.post('/create', response_model=User)
def create_user(user: UserCreate, user_service: UserService = Depends()):
    if user_service.get_user_by_email(user.email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user exists with this email')
    if user_service.get_user_by_name(user.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user exists with this nickname')
    return user_service.create_user(user)


@router.put('/{user_id}/update', response_model=User)
def update_user(
        user_id: int,
        update_data: UserUpdate,
        user_service: UserService = Depends()
):
    user_by_email = user_service.get_user_by_email(update_data.email)
    if user_by_email and user_by_email.id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user exists with this email')
    user_by_name = user_service.get_user_by_name(update_data.name)
    if user_by_name and user_by_name.id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user exists with this nickname')
    return user_service.update_user(user_id, update_data)


@router.delete('/{user_id}/delete', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, user_service: UserService = Depends()):
    user_service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
