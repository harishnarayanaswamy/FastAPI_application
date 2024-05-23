"""Banner model"""

import uuid
import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from pydantic import BaseModel, Field


class Banner(BaseModel):
    id: str = str(uuid.uuid4())
    name: str = Field(default=None, min_length=4, max_length=20)
    banner: str
    is_active: str = Field(default=True)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Banner')
def get_banners():
    response = table.scan(FilterExpression=Attr('is_active').eq(True))
    return response.get('Items', [])

def get_banner(banner_id, active='yes'):
    response = table.get_item(Key={"id": banner_id})
    return response.get('Item', None)

def delete_banner(banner_id):
    table.delete_item(Key={"id": banner_id})

def create_banner(item):
    try:
        existing_item = get_banner(item['id'])
    except Exception as e:
        print(e)
        existing_item = None
    if not existing_item:
        try:
            response = table.put_item(Item=item)
        except ClientError as e:
            print(str(e))
            return False, str(e)
    return item, "" # Return the created item itself
