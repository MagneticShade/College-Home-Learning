# mypy
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .Permissions import Permissions
    from .Roles import Roles


class Permissions_and_roles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    role_id: int = Field(foreign_key="roles.id")
    permission_id: int = Field(foreign_key="permissions.id")
    role: "Roles" = Relationship(back_populates="permissions")
    permission: "Permissions" = Relationship(back_populates="roles")
