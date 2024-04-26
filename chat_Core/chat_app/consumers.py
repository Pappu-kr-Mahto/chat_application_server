from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import * 
import json
class ChatComsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Testing connection")
        self.userId = self.scope['url_route']['kwargs']['userId']
        self.userRooms = await database_sync_to_async(list)(ChatRoom.objects.filter(members = self.userId))

        for room in self.userRooms:
            await self.channel_layer.group_add( room.roomId , self.channel_name)
        
        print(self.userRooms)
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        text_data = json.loads(text_data)
        roomId = text_data['roomId']
        message = text_data['message']
        await self.channel_layer.group_send(
			roomId,
			{
                'type': 'chat_message',
				'message': text_data
			}
		)
        # return super().receive(message, bytes_data)

    async def disconnect(self, code):
        return super().disconnect(code)
    
    async def chat_message(self, event):
        # Send the message to the client
        message = event['message']
        await self.send(text_data=json.dumps(message))