from django.urls import path
from .consumers import ChatComsumer

ws_urlpatterns = [
    path('ws/chat/',ChatComsumer.as_asgi())
]