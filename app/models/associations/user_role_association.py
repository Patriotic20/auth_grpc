from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, func, DateTime
from core.mixins.id_int_pk import IdIntPk
from datetime import datetime

class UserRoleAssociation(IdIntPk, Base):
    __tablename__ = "user_role_associations"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"), nullable=False)
    
    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )