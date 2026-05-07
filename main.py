from typing import List

from fastapi import FastAPI
from Endpoints.Dog_END import router_dogs
from db import  SessionDep, create_all_tables
from sqlmodel import select

app = FastAPI(lifespan=create_all_tables)
app.include_router(router_dogs)


