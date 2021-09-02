import uvicorn
from fastapi import FastAPI
from settings import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worl"}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True,
        host=settings.host,
        port=settings.port,
)