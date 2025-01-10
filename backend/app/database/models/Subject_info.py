from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Subjects import Subjects


# type:ignore
class Subject_info(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    instances: list["Subjects"] = Relationship(back_populates="name")
