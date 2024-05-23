"""Common response models"""

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: str = "error"
    msg: str


class CommonSuccessResponse(BaseModel):
    status: str = "success"
    msg: str