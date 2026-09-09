from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.enrollment_schema import (EnrollmentCreate, EnrollmentResponse)
from app.usecases.enrollment_usecase import (UserNotFoundError, CourseNotFoundError, EnrollmentAlreadyExistsError, EnrollmentUseCase)

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

def get_enrollment_usecase(db: Session = Depends(get_db)) -> EnrollmentUseCase:
    enrollment_repository = EnrollmentRepository(db)
    user_repository = UserRepository(db)
    course_repository = CourseRepository(db)

    return EnrollmentUseCase(enrollment_repository, user_repository, course_repository)

@router.post("", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)

def create_enrollment(data: EnrollmentCreate, usecase: EnrollmentUseCase = Depends(get_enrollment_usecase)):
    try:
        return usecase.create(data)

    except EnrollmentAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))

    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))  

    except CourseNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))  