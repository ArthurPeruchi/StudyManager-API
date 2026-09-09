from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.course import Course

class CourseRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, course: Course):
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)

        return course

    def get_all(self) -> list[Course]:
        statement = select(Course)

        return list(self.db.scalars(statement).all())

    def get_by_id(self, course_id: int) -> Course | None:
        statement = select(Course).where(Course.id == course_id) 

        return self.db.scalar(statement)

    def get_by_title(self, course_title: str) -> Course | None:
        statement = select(Course).where(Course.title == course_title)

        return self.db.scalar(statement)

    def update(self, course: Course):
        self.db.commit()
        self.db.refresh(course)

        return course

    def delete(self, course: Course) -> None:
        self.db.delete(course)
        self.db.commit()