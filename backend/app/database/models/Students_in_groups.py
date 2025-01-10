from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Groups import Groups
    from .Users import Users

#type:ignore
class Students_in_groups(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_id: int = Field(default=None, foreign_key="users.id")
    group_id: int = Field(default=None, foreign_key="groups.id")
    book_number: str
    student: "Users" = Relationship(back_populates="group")
    group: "Groups" = Relationship(back_populates="students")
