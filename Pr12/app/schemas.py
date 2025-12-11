import uuid

from fastapi_users import schemas
from pydantic import BaseModel, Field
from typing import Optional

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass


class ImageProcessingOptions(BaseModel):
    resize: Optional[str] = Field(None, description="Example: '1920x1080'")
    convert_to: Optional[str] = Field(None, description="Example: 'png', 'jpeg', webp'")
    greyscale: Optional[bool] = Field(False, description="Convert to greyscale")
    flip: Optional[bool] = Field(False, description="horizontal or vertical")