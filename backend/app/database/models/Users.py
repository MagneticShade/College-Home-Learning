from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Groups import Groups
    from .Roles import Roles
    from .Students_in_groups import Students_in_groups
    from .Subjects import Subjects


# type:ignore
class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    middle_name: str
    surname: str
    role_id: int = Field(foreign_key="roles.id")

    role: "Roles" = Relationship(back_populates="users")
    curating: list["Groups"] = Relationship(back_populates="curator")
    group: "Students_in_groups" = Relationship(back_populates="student")
    subjects: list["Subjects"] = Relationship(back_populates="teacher")
