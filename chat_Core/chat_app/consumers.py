from channels.generic.websocket import AsyncWebsocketConsumer

class ChatComsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Testing connection")
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        await self.send(text_data)
        return super().receive(text_data, bytes_data)

    async def disconnect(self, code):
        return super().disconnect(code)