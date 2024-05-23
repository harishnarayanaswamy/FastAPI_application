"""Shop model."""

import uuid
from pydantic import BaseModel, Field
from boto3.dynamodb.conditions import Attr
import boto3


class Shop(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    address: str
    is_active: bool = Field(default=True)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Shop')
def get_shops():
    response = table.scan(FilterExpression=Attr('is_active').eq(True))
    return response.get('Items', [])

def get_shop(shop_id):
    response = table.get_item(Key={"id": shop_id})
    return response.get('Item', None)
