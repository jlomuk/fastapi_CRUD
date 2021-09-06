from fastapi import APIRouter, Depends

from schemas.user_schemas import Token
from services.user_services import UserService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/auth',
    tags=['authenticate']
)


@router.post('/login', response_model=Token)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        user_service: UserService = Depends()
):
    return user_service.login(form_data.username, form_data.password)