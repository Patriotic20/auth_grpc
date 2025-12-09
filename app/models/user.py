from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

from core.mixins.id_int_pk import IdIntPk
from core.mixins.timestamp_mixin import TimestampMixin
from .base import Base

if TYPE_CHECKING:
    from .role import Role

class User(IdIntPk, TimestampMixin, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    roles: Mapped[list["Role"]] = relationship(
        "Role",
        secondary="user_role_associations",   
        back_populates="users"
    )
