from sqlmodel import Field, SQLModel
from Enums.DogEnums import StatusEnum
from datetime import datetime
from typing import Optional

class Dog(SQLModel):
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str
    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )

class DogID(Dog, table=True):
    __tablename__ = "Dogs"
    id : int | None = Field(default=None, primary_key=True,gt=0)
    status: StatusEnum = Field(default=StatusEnum.active)

class DogUpdate(SQLModel):
    name: Optional[str] = None
    size: Optional[str] = None
    dangerous: Optional[bool] = None
    sterilized: Optional[bool] = None
    breed: Optional[str] = None
    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )