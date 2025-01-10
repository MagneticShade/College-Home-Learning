from sqlmodel import SQLModel

from .Groups import Groups
from .Permissions import Permissions
from .Permissions_and_roles import Permissions_and_roles
from .Roles import Roles
from .Students_in_groups import Students_in_groups
from .Subject_info import Subject_info
from .Subjects import Subjects
from .Users import Users

__all__ = [
    "SQLModel",
    "Groups",
    "Permissions",
    "Permissions_and_roles",
    "Roles",
    "Students_in_groups",
    "Subject_info",
    "Subjects",
    "Users",
]
