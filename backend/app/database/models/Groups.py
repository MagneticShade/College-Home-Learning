from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Students_in_groups import Students_in_groups
    from .Subjects import Subjects
    from .Users import Users

#type:ignore
class Groups(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    group_name: str
    curator_id: int = Field(default=None, foreign_key="users.id")
    speciality_code: str
    curator: "Users" = Relationship(back_populates="curating")
    students: list["Students_in_groups"] = Relationship(back_populates="group")
    subjects: "Subjects" = Relationship(back_populates="group")
