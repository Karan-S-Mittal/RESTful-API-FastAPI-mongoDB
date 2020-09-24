from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, le=4)
    gpa: float = Field(..., ge=0, le=10.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Karan Mittal",
                "email": "karanmittal@example.com",
                "course_of_study": "Computer Science Engineering",
                "year": 4,
                "gpa": "7.8",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Name Update",
                "email": "karanmittal@example.com",
                "course_of_study": "Computer Science Engineering",
                "year": 4,
                "gpa": "7.8",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message, 
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }

