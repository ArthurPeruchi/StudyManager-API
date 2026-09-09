from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.controllers.course_controller import router as course_router
from app.controllers.enrollment_controller import router as enrollment_router

app = FastAPI(
    title="StudyManager API",
    description="API for managing users, courses and enrollments",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)