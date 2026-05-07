from sqlmodel import Session, select

from Modelo.model import Dog, DogID, DogUpdate

def create_dog(dog: Dog, session: Session):
    new_dog = DogID.model_validate(dog)
    session.add(new_dog)
    session.commit()
    session.refresh(new_dog)
    return new_dog

def show_all_dogs(session: Session):
    statement = select(DogID)
    return session.exec(statement).all()

def show_all_actived(session: Session):
    statement = select(DogID).where(DogID.status == "active")
    return session.exec(statement).all()

def show_all_deleted(session: Session):
    statement = select(DogID).where(DogID.status == "inactive")
    return session.exec(statement).all()

def find_one_dog(id: int, session: Session):
    dog = session.get(DogID, id)
    if not dog or dog.status != "active":
        return None
    return dog

def update_one_dog(id: int, new_dog: DogUpdate, session: Session):
    dog = find_one_dog(id, session)
    if dog is None:
        return None
    dog_data = new_dog.model_dump(exclude_unset=True)
    dog.sqlmodel_update(dog_data)
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog

def delete_one_dog(id: int, session: Session):
    dog = session.get(DogID, id)
    if not dog or dog.status == "inactive":
        return None
    dog.status = "inactive"
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog

def restore_one_dog(id: int, session: Session):
    dog = session.get(DogID, id)
    if not dog:
        return None
    dog.status = "active"
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog