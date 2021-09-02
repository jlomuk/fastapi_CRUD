from fastapi.routing import APIRouter

router = APIRouter(
    prefix='/books',
    tags=['books']
)


@router.get('/')
async def get_list_books():
    return {'book': 'book'}