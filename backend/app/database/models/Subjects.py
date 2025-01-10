from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Groups import Groups
    from .Subject_info import Subject_info
    from .Users import Users

#type:ignore
class Subjects(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    subject_name_id: int = Field(foreign_key="users.id")
    teacher_id: int = Field(foreign_key="users.id")
    group_id: int = Field(foreign_key="groups.id")

    name: "Subject_info" = Relationship(back_populates="instances")
    group: "Groups" = Relationship(back_populates="subjects")
    teacher: "Users" = Relationship(back_populates="subjects")
