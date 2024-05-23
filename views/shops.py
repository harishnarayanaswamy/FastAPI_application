"""Shops views."""

from typing import Annotated, List
from fastapi import APIRouter, Body, Depends, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from commons.common_response_models import ErrorResponse, CommonSuccessResponse
from models.shop import get_shops, get_shop
from models.user import User
from utils.access_token_utils import get_current_active_user


router = APIRouter()

class ShopParams(BaseModel):
    id: str
    name: str
    address: str

class ShopSuccessResponse(BaseModel):
    shops:List[ShopParams] = []


@router.get(
    "/api/shops",
    responses={
        400: {"model": ErrorResponse}, 
        500: {"model": ErrorResponse},
        200: {"model": ShopSuccessResponse}
    }
)
async def all_shops(
    user: User = Depends(get_current_active_user)
):
    """Get list of all shops."""
    return ShopSuccessResponse(shops=get_shops())
        

@router.post(
    "/api/users/shop",
    responses={
        400: {"model": ErrorResponse}, 
        500: {"model": ErrorResponse},
        200: {"model": ShopSuccessResponse}
    }
)
async def update_shop(
    shop_id: Annotated[str, Body(embed=True)],
    response: Response,
    user: User = Depends(get_current_active_user),
):
    """Update user with shop."""
    shop = get_shop(shop_id=shop_id)
    if not shop:
        response.status_code = 400
        return ErrorResponse(
            msg="shop does not exisit."
        )
    if shop_id != user['shop']:
        print("updated in the database")
        user['shop'] = shop['id']
    return CommonSuccessResponse(
        msg="User shop is updated."
    )

