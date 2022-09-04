import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connecting")

        await self.accept()

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        print('принты')
        print(self.room_name, 'room name')
        print(self.room_group_name, 'group name')
        print(self.channel_name, 'chanel name')
        print(self.channel_layer, 'channel layer')

        # await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    # # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # # Receive message from room group
    # async def chat_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message
    #     }))


# from channels.consumer import SyncConsumer

# class EchoConsumer(SyncConsumer):

#     def websocket_connect(self, event):
#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })


# # Импорт для работы с JSON
# import json 
# # Импорт для асинхронного программирования
# from channels.generic.websocket import AsyncWebsocketConsumer
# # Импорт для работы с БД в асинхронном режиме
# from channels.db import database_sync_to_async
# # Импорт модели сообщений
# from .models import Message
 
 
# # Класс ChatConsumer
# class ChatConsumer(AsyncWebsocketConsumer):
    
#     # Метод подключения к WS
#     async def connect(self):
#         # Назначим пользователя в комнату
#         self.room_group_name = "1"
#         # Добавляем новую комнату
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         # Принимаем подключаем
#         await self.accept()
 
#     # Метод для отключения пользователя
#     async def disconnect(self, close_code):
#         # Отключаем пользователя
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
 
#     # Декоратор для работы с БД в асинхронном режиме
#     @database_sync_to_async
#     # Функция для создания нового сообщения в БД
#     def new_message(self, message):
#         # Создаём сообщение в БД
#         Message.objects.create(text=message)
 
#     # Принимаем сообщение от пользователя
#     async def receive(self, text_data=None, bytes_data=None):
#         # Форматируем сообщение из JSON
#         text_data_json = json.loads(text_data)
#         # Получаем текст сообщения
#         message = text_data_json['message']
        
#         # Добавляем сообщение в БД 
#         await self.new_message(message=message)
        
#         # Отправляем сообщение 
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#             }
#         )
    
#     # Метод для отправки сообщения клиентам
#     async def chat_message(self, event):
#         # Получаем сообщение от receive
#         message = event['message']
#         # Отправляем сообщение клиентам
#         await self.send(text_data=json.dumps({
#             'message': message,
#         }, ensure_ascii=False))




# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         # self.room_name = self.scope['url_route']['kwargs']['room_name']
#         # self.room_group_name = 'chat_%s' % self.room_name
#         # self.room_group_name = 'chat_%s' % self.scope['room_name']


#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             'chat',
#             self.channel_name
#         )

#         self.accept()

    # def disconnect(self, close_code):
    #     # Leave room group
    #     async_to_sync(self.channel_layer.group_discard)(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    # # Receive message from WebSocket
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     # Send message to room group
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # # Receive message from room group
    # def chat_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))