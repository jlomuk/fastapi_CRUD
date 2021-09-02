from fastapi.routing import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
async def get_list_users():
    return {'user': 'user'}
