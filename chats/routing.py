from django.urls import re_path
from django.urls import path
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # path("ws/chat/<int:room_name>", consumers.ChatConsumer.as_asgi()),
    # re_path(r'wss/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()), #local
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()), #heroku
]