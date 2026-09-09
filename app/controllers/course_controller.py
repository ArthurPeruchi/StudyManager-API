from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.course_repository import CourseRepository
from app.schemas.course_schema import (CourseCreate, CourseResponse, CourseUpdate)
from app.usecases.course_usecase import (CourseAlreadyExistsError, CourseNotFoundError, CourseUseCase)

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_course_usecase(db: Session = Depends(get_db)) -> CourseUseCase:
    repository = CourseRepository(db)

    return CourseUseCase(repository)

@router.post("", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)

def create_course(data: CourseCreate, usecase: CourseUseCase = Depends(get_course_usecase)):
    try:
        return usecase.create(data)

    except CourseAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.get("", response_model=list[CourseResponse], status_code=status.HTTP_200_OK)

def get_courses(usecase: CourseUseCase = Depends(get_course_usecase)):
    return usecase.get_all()

@router.get("/{id}", response_model=CourseResponse, status_code=status.HTTP_200_OK)

def get_course_by_id(id: int, usecase: CourseUseCase = Depends(get_course_usecase)):
    try:
        return usecase.get_by_id(id)

    except CourseNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))  

@router.put("/{id}", response_model=CourseResponse, status_code=status.HTTP_200_OK)

def update_course_by_id(id: int, data: CourseUpdate, usecase: CourseUseCase = Depends(get_course_usecase)):
    try:
        return usecase.update(id, data)

    except CourseAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))

    except CourseNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))  
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def delete_course_by_id(id: int, usecase: CourseUseCase = Depends(get_course_usecase)):
    try:
        usecase.delete(id)

    except CourseNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))