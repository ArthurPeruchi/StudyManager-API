from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment

class EnrollmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, enrollment: Enrollment):
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)

        return enrollment

    def find_by_user_and_course(self, user_id: int, course_id: int):
        statement = select(Enrollment).where(Enrollment.user_id == user_id, Enrollment.course_id == course_id)

        return self.db.scalar(statement)