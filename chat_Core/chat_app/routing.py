from django.urls import path
from .consumers import ChatComsumer

ws_urlpatterns = [
    path('ws/chat/<int:userId>',ChatComsumer.as_asgi())
]