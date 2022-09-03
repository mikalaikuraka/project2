from django.urls import re_path
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("wss/chat/<int:room_name>", consumers.ChatConsumer.as_asgi()),
    # re_path(r'wss/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]