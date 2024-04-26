from django.urls import path
from . import views
urlpatterns = [
    path('api/signup/',views.signup,name="signup"),
    path('api/login/',views.login,name="login"), 

    path('api/getAllChatUsers/',views.getAllChatUsers,name="getAllChatUsers"), 
    path('api/getAllUsers/',views.getAllUsers,name="getAllUsers"), 
    path('api/createroom/', views.createroom, name='createroom'),
    path('api/chatmessages/<roomId>/', views.chatmessages, name='chatmessages'),
]
