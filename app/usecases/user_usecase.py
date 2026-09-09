from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import (UserCreate, UserUpdate, UserWithCoursesResponse)

class UserNotFoundError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, data: UserCreate) -> User:
        existing_user = self.repository.get_by_email(data.email)

        if existing_user:
            raise EmailAlreadyExistsError("[!] Email já cadastrado.")

        user = User(name=data.name, email=data.email)

        return self.repository.create(user)

    def get_all(self) -> list[User]:
        return self.repository.get_all()

    def get_by_id(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)

        if not user:
            raise UserNotFoundError("[!] Usuário não encontrado.")

        return user

    def update(self, user_id: int, data: UserUpdate) -> User:
        user = self.get_by_id(user_id)

        existing_user = self.repository.get_by_email(data.email)

        if existing_user and existing_user.id != user_id:
            raise EmailAlreadyExistsError("[!] Email já cadastrado.")

        user.name = data.name
        user.email = data.email

        return self.repository.update(user)

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)

        if not user:
            raise UserNotFoundError("[!] Usuário não encontrado.")

        self.repository.delete(user)

    def get_user_with_courses(self, user_id: int) -> UserWithCoursesResponse:
        user = self.repository.get_with_courses(user_id)

        if not user:
            raise UserNotFoundError("[!] Usuário não encontrado.")

        courses = [enrollment.course for enrollment in user.enrollments]

        return UserWithCoursesResponse(user=user, courses=courses)