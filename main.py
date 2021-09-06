import uvicorn
from endpoints import router
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from settings import settings

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True,
        host=settings.host,
        port=settings.port,
)
