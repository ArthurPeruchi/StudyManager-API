from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.enrollment import Enrollment

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    workload: Mapped[int] = mapped_column(Integer, nullable=False)
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="course")