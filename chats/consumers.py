# from channels.consumer import AsyncConsumer
# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# class EchoConsumer(AsyncWebsocketConsumer):

#     async def websocket_connect(self, event):

#         await self.accept()

#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
        
#         await self.send({
#             "type": "chat_message",
#             "message": message,
#         })

#     async def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         await self.send(event =json.dumps({
#             'message': message
#         }))

    


# import json
# from chat import asgi
# from channels.generic.websocket import AsyncWebsocketConsumer
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
        
#         print("1")
#         self.room_name = self.scope.get("url_route").get("kwargs").get("room_name")
#         print("2")
#         self.room_group_name = 'chat_%s' % self.room_name
#         print("3")

        

#         # 4 строки ниже сносят вебсокет, 
#         # но если их закомментить, то вебсокет 
#         # работает но ничего не отображается 
#         # и не подключается по tcp

#         # await self.channel_layer.group_add(
#         #     self.room_group_name,
#         #     self.channel_name
#         # )

#         try:
#             await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#             )
            
#         except Warning:
#             print(Warning)

#         print("4")
        
        
#         # print('принты')
#         # print(self.scope, 'self.scope')
#         # print(self.room_name, 'room name')
#         # print(self.room_group_name, 'group name')
#         # print(self.channel_name, 'chanel name')
#         # print(self.channel_layer, 'channel layer')

#         await self.accept()

#         print("5")
#     # async def disconnect(self, close_code):
#     #     # Leave room group
#     #     await self.channel_layer.group_discard(
#     #         self.room_group_name,
#     #         self.channel_name
#     #     )

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         print('6')
#         text_data_json = json.loads(text_data)
#         print("7")
#         message = text_data_json['message']
#         print("8")
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#         print("9")

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']
#         print("10")
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
#         print("11")









# from channels.consumer import AsyncConsumer

# class EchoConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })

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




import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # self.room_group_name = 'chat_%s' % self.scope['room_name']


        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            'chat',
            self.channel_name
        )

        # self.send({
        #     'type':'websocket.accept'
        # })

        self.accept()

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