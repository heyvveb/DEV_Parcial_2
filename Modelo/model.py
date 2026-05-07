from sqlmodel import Field, SQLModel

from datetime import datetime


class Dog(SQLModel, table = True):
    __tablename__ = "Dogs"

    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )