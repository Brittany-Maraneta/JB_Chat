# myproject/routing.py

from django.urls import re_path
from . import consumers  # Import the consumer
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),  # Room-based chat URL
]
