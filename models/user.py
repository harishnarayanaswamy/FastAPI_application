"""User model"""

import uuid
import boto3
from botocore.exceptions import ClientError
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    userId: str = str(uuid.uuid4())
    name: str = Field(default=None, min_length=4, max_length=20)
    email: EmailStr | None = Field(default=None)
    phone_number: str = Field(default=None, max_length=10, min_length=10)
    address: str = Field(default=None, max_items=250)
    shop: str = Field(default=None)
    is_active: bool = Field(default=True)
    created_at: str = None
    updated_at: str = None


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')
def get_users():
    response = table.scan()
    return response.get('Items', [])

def get_user(phone_number):
    response = table.get_item(Key={"phone_number": phone_number})
    return response.get('Item', None)

def delete_user(phone_number):
    table.delete_item(Key={"phone_number": phone_number})
