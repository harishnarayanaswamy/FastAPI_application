"""Help Videos views."""

from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from models.help_videos import get_videos
from commons.common_response_models import ErrorResponse
from models.user import User
from utils.access_token_utils import get_current_active_user


router = APIRouter()

class help_video_params(BaseModel):
    video_id: str
    name: str

class help_video_success_response(BaseModel):
    videos:List[help_video_params] = []


@router.get(
    "/api/helpvideos",
    responses={
        400: {"model": ErrorResponse}, 
        500: {"model": ErrorResponse},
        200: {"model": help_video_success_response}
    }
)
async def all_help_videos(
    user: User = Depends(get_current_active_user)
):
    """Get list of all shops."""
    return help_video_success_response(videos=get_videos())
