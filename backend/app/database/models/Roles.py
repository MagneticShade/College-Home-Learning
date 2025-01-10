from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Permissions_and_roles import Permissions_and_roles
    from .Users import Users

#type:ignore
class Roles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    users: list["Users"] = Relationship(back_populates="role")
    permissions: list["Permissions_and_roles"] = Relationship(back_populates="role")
