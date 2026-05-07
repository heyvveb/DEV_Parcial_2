from fastapi import APIRouter, HTTPException
from typing import List
from Modelo.model import Dog, DogID, DogUpdate
from db import SessionDep
from Operations.Dog_OP import *

router_dogs = APIRouter(prefix="/Dogs", tags=["Dogs"])

@router_dogs.post("/", response_model=Dog)
async def create_dog(dog: Dog, session: SessionDep):
    return create_dog(dog, session)

@router_dogs.get("/", response_model=List[DogID])
async def get_all_dogs(session: SessionDep):
    return show_all_dogs(session)


@router_dogs.get("/{id}", response_model=DogID)
async def get_dog(id: int, session: SessionDep):
    dog = find_one_dog(id, session)
    if dog is None:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog


@router_dogs.put("/{id}", response_model=DogID)
async def update_dog(id: int, new_dog: DogUpdate, session: SessionDep):
    dog = update_one_dog(id, new_dog, session)
    if dog is None:
        raise HTTPException(status_code=404, detail="dog not found or inactive")
    return dog


@router_dogs.delete("/{id}", response_model=DogID)
async def delete_dog(id: int, session: SessionDep):
    dog = delete_one_dog(id, session)
    if dog is None:
        raise HTTPException(status_code=404, detail="dog not found or already inactive")
    return dog



@router_dogs.patch("/{id}/restore", response_model=DogID)
async def restore_dog(id: int, session: SessionDep):
    dog = restore_one_dog(id, session)
    if dog is None:
        raise HTTPException(status_code=404, detail="dog not found")
    return dog