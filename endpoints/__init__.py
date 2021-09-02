from fastapi.routing import APIRouter
from endpoints.user_api import router as user_api
from endpoints.book_api import router as book_api

router = APIRouter()
router.include_router(user_api)
router.include_router(book_api)