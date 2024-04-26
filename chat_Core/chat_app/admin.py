from django.contrib import admin
from .models import CustomUserModel, ChatRoom, ChatMessage
# Register your models here.

admin.site.register(CustomUserModel)
admin.site.register(ChatRoom)
admin.site.register(ChatMessage)

