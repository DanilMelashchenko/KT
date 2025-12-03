from pydantic import BaseModel, EmailStr, ConfigDict

class StudentCreate(BaseModel):
    name: str
    group: str
    grade: float
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    group: str
    grade: float
    email: str

    model_config = ConfigDict(from_attributes=True)