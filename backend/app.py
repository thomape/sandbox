from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import DBConnection
import uvicorn
from api import test_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(test_api.router)



if __name__ == '__main__':
    uvicorn.run('app:app',port=8000,reload=True)