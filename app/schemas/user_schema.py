from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.schemas.course_schema import CourseResponse

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr

class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserWithCoursesResponse(BaseModel):
    user: UserResponse
    courses: list[CourseResponse]