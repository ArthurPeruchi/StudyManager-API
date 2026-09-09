from app.models.enrollment import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.enrollment_schema import EnrollmentCreate

class CourseNotFoundError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class EnrollmentAlreadyExistsError(Exception):
    pass

class EnrollmentUseCase:

    def __init__(self, enrollment_repository: EnrollmentRepository, user_repository: UserRepository, course_repository: CourseRepository):
        self.enrollment_repository = enrollment_repository
        self.user_repository = user_repository
        self.course_repository = course_repository


    def create (self, data: EnrollmentCreate):
        user = self.user_repository.get_by_id(data.user_id)

        if not user:
            raise UserNotFoundError("[!] Usuário não encontrado.")

        course = self.course_repository.get_by_id(data.course_id)

        if not course:
            raise CourseNotFoundError("[!] Curso não encontrado.")

        existing_enrollment = self.enrollment_repository.find_by_user_and_course(data.user_id, data.course_id)

        if existing_enrollment:
            raise EnrollmentAlreadyExistsError("[!] Usuário já está matriculado neste curso.")

        enrollment = Enrollment(user_id=data.user_id, course_id=data.course_id)

        return self.enrollment_repository.create(enrollment)