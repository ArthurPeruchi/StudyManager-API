from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import (UserCreate, UserResponse, UserUpdate, UserWithCoursesResponse)
from app.usecases.user_usecase import (EmailAlreadyExistsError, UserNotFoundError, UserUseCase)

router = APIRouter(prefix="/users", tags=["Users"])

def get_user_usecase(db: Session = Depends(get_db)) -> UserUseCase:
    repository = UserRepository(db)

    return UserUseCase(repository)

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)

def create_user(data: UserCreate, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        return usecase.create(data)

    except EmailAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.get("", response_model=list[UserResponse], status_code=status.HTTP_200_OK)

def get_users(usecase: UserUseCase = Depends(get_user_usecase)):
    return usecase.get_all()

@router.get("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)

def get_user_by_id(id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        return usecase.get_by_id(id)

    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.get("/{id}/courses", response_model=UserWithCoursesResponse, status_code=status.HTTP_200_OK)
def get_user_with_courses(id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        return usecase.get_user_with_courses(id)

    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))

@router.put("/{id}", response_model=UserUpdate, status_code=status.HTTP_200_OK)

def update_user_by_id(data: UserUpdate, id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        return usecase.update(id, data)

    except EmailAlreadyExistsError as error:
        raise HTTPException(status_code=409, detail=str(error))

    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))  

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def delete_user_by_id(id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    try:
        usecase.delete(id)

    except UserNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))