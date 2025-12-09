from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base import Base
from core.mixins.id_int_pk import IdIntPk
from core.mixins.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .role import Role

class Permission(IdIntPk, TimestampMixin ,Base):
    __tablename__ = "permissions"
    
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    resource: Mapped[str] = mapped_column(String(50), nullable=False)
    action: Mapped[str] = mapped_column(String(50), nullable=False)
    
    
    roles: Mapped[list["Role"]] = relationship(
        "Role",
        secondary="role_permission_associations",
        back_populates="permissions"
    )