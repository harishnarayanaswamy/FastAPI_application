"""Profile views."""

import json
import re
from typing import Annotated
from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

from commons.common_response_models import CommonSuccessResponse, ErrorResponse
from models.user import User
from utils.access_token_utils import get_current_active_user


router = APIRouter()


class profile_success_response(BaseModel):
    status: str
    email: EmailStr = None
    phone_number: str
    name: str = None
    address: str = None
    

@router.get(
    "/api/auth/profile",
    responses={
        400: {"model": ErrorResponse}, 
        500: {"model": ErrorResponse},
        200: {"model": profile_success_response}
    }
)
async def profile_details(
    user: User = Depends(get_current_active_user),
):
    """Get profile details."""
    return JSONResponse(status_code=200, content={
        "status": "success",
        "email": user['email'],
        "phone_number": user['phone_number'],
        "name": user['name'],
        "address": user['address']
    })


def is_valid_email(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.search(regex, email)):
        return True
    return False
