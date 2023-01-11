from datetime import date
from pydantic import BaseModel
from app.models.person import Sex


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
