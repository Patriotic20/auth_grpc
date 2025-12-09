from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

from core.mixins.id_int_pk import IdIntPk
from core.mixins.timestamp_mixin import TimestampMixin
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .permission import Permission

class Role(IdIntPk, TimestampMixin, Base):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary="user_role_associations",
        back_populates="roles"
    )

    permissions: Mapped[list["Permission"]] = relationship(
        "Permission",
        secondary="role_permission_associations",
        back_populates="roles"
    )
