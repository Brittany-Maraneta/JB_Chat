from channels.db import database_sync_to_async
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
import json

# This makes sure to run these database calls in sync mode within an async function
@database_sync_to_async
def get_or_create_chat_room(room_name):
    return ChatRoom.objects.get_or_create(name=room_name)

@database_sync_to_async
def save_message(room, user, message_content):
    # Fetch the User instance based on the username string
    user_instance = User.objects.get(username=user)
    return Message.objects.create(room=room, user=user_instance, content=message_content)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Get or create the chat room asynchronously
        self.room, created = await get_or_create_chat_room(self.room_name)

        # Join the WebSocket group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the WebSocket group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']

        # Save the message asynchronously, fetching the User instance
        await save_message(self.room, user, message)

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user,
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'user': user,
            'message': message,
        }))
