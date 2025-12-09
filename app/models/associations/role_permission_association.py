from models.base import Base
from core.mixins.id_int_pk import IdIntPk
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, DateTime, func
from datetime import datetime


class RolePermissionAssociation(IdIntPk, Base):
    __tablename__ = "role_permission_associations"
    
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    permission_id: Mapped[int] = mapped_column(Integer, ForeignKey("permissions.id"), nullable=False)
    
    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
