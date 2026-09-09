from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course_schema import CourseCreate, CourseUpdate

class CourseNotFoundError(Exception):
    pass

class CourseAlreadyExistsError(Exception):
    pass

class CourseUseCase:

    def __init__ (self, repository: CourseRepository):
        self.repository = repository

    def create(self, data: CourseCreate):
        existing_course = self.repository.get_by_title(data.title)

        if existing_course:
            raise CourseAlreadyExistsError("[!] Curso já cadastrado.")

        course = Course(title=data.title, description=data.description, workload=data.workload)

        return self.repository.create(course)

    def get_all(self) -> list[Course]:
        return self.repository.get_all()

    def get_by_id(self, course_id: int) -> Course:
        course = self.repository.get_by_id(course_id)

        if not course:
            raise CourseNotFoundError("[!] Curso não encontrado.")

        return course

    def update(self, course_id: int, data: CourseUpdate):
        course = self.get_by_id(course_id)

        existing_course = self.repository.get_by_title(data.title)

        if existing_course and existing_course.id != course_id:
            raise CourseAlreadyExistsError("[!] Curso já cadastrado.")

        course.title = data.title
        course.description = data.description
        course.workload = data.workload

        return self.repository.update(course)

    def delete(self, course_id: int) -> None:
        course = self.get_by_id(course_id)

        if not course:
            raise CourseNotFoundError("[!] Curso não encontrado.")

        self.repository.delete(course)