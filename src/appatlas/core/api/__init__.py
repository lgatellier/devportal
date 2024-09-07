from fastapi import FastAPI
from appatlas.core import fastapi_app

api_app = FastAPI()
fastapi_app.mount("/api", api_app)
