from fastapi.routing import APIRouter

from schemas.user_schemas import User

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/', response_model=User)
async def get_list_users():
   pass