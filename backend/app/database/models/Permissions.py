from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Permissions_and_roles import Permissions_and_roles

#type:ignore
class Permissions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    permission_name: str
    permission_key: int
    roles: list["Permissions_and_roles"] = Relationship(back_populates="permission")
