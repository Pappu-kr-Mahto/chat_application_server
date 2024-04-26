from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from shortuuidfield import ShortUUIDField

# Create your models here.

class CustomUserModel(AbstractUser):
    username = None
    profile_img = models.ImageField(upload_to="profile_images",null=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ChatRoom(models.Model):
    roomId = ShortUUIDField(primary_key=True)
    type = models.CharField(max_length=20, default='DM')
    name=models.CharField(max_length=50,null=True, blank=True)
    members= models.ManyToManyField(CustomUserModel, related_name='chat_members')
    onlineMembers = models.ManyToManyField(CustomUserModel, related_name='online_chat_members')
    createdAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.roomId + '--' + str(self.name)
    
class Messages(models.Model):
    chatRoomId = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    sender = models.ForeignKey(CustomUserModel , on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.message
