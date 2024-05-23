"""Banner views."""

from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from commons.common_response_models import ErrorResponse
from models.banner import get_banners
from models.user import User
from utils.access_token_utils import get_current_active_user


router = APIRouter()


class banner_details(BaseModel):
    id: str
    name: str
    banner: str


class get_banners_response(BaseModel):
    banners: List[banner_details] = []


def get_all_banners():
    """Get list of all banners."""
    return get_banners_response(banners=get_banners())


@router.get(
    "/api/banners",
    responses={
        400: {"model": ErrorResponse}, 
        500: {"model": ErrorResponse},
        200: {"model": get_banners_response}
    }
)
async def all_banners(
    user: User = Depends(get_current_active_user)
):
    """Get list of all shops."""
    return get_all_banners()
        
