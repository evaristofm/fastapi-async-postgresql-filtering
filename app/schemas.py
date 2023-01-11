from datetime import date
from typing import Optional, TypeVar
from fastapi import HTTPException
from pydantic import BaseModel, validator
from app.models.person import Sex

T = TypeVar("T")

class PersonCreate(BaseModel):
    name: str
    sex: Sex
    birth_date: date
    birth_place: str
    country: str

    # sex validation
    @validator("sex")
    def sex_validation(cls, v) :
        if hasattr(Sex, v):
            raise HTTPException(status_code=400, detail="Invalid input sex")
        return v


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
