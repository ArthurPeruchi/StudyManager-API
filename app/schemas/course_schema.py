from pydantic import BaseModel, Field

class CourseCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str
    workload: int

class CourseUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str
    workload: int

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str | None
    workload: int

    class Config:
        from_attributes = True