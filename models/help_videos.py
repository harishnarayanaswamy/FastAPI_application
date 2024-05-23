"""Help videos model"""

import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from pydantic import BaseModel, Field


class HelpVideo(BaseModel):
    video_id: str
    name: str
    is_active: str = Field(default=True)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('help_video')
def get_videos():
    response = table.scan(FilterExpression=Attr('is_active').eq(True))
    return response.get('Items', [])

def get_video(video_id):
    response = table.get_item(Key={"video_id": video_id})
    return response.get('Item', None)

def delete_video(video_id):
    table.delete_item(Key={"bannerId": video_id})

def create_video(item):
    try:
        existing_item = get_video(item['video_id'])
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
