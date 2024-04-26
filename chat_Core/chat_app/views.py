from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


# Create your views here.


@api_view(['POST'])
def signup(request):
    try:
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user=CustomUserModel.objects.create_user(email = serializer.validated_data['email'] , first_name=serializer.validated_data['first_name'] ,last_name=serializer.validated_data['last_name'] , password = serializer.validated_data['password'])

            return Response({"success":"Account Created successfully","username":request.data['first_name'],"email":request.data['email']},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Email Already exists'},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error":'Internal server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def login(request):
    try:
        email= request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUserModel.objects.filter(email=email).first()
        print(user.username)
        if user is not None:
            temp = authenticate(email=user.email, password=password)
            if temp is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                        'user':email,
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    })
        return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getAllChatUsers(request):
    userObj = CustomUserModel.objects.filter(email = request.user).values()
    userdata = ChatRoom.objects.filter(members=request.user).values()
    return Response({'user':userObj , 'data':userdata})

@api_view(['GET'])
def getAllUsers(request):
    userData =CustomUserModel.objects.filter(is_staff=False).values('id','first_name','last_name','email')
    return Response({'data': userData})


@api_view(['POST'])
def createroom(request):
    userId = request.data
    userObj = CustomUserModel.objects.get(email = request.user)
    for id in userId:
        tempUser = CustomUserModel.objects.get(id=id)
        obj =ChatRoom.objects.create(name = tempUser.first_name)
        obj.members.add(userObj)
        obj.members.add(tempUser)
        obj.save()
    return Response({'success':'working'})

@api_view(['GET'])
def chatmessages(request,roomId):
    print(roomId)
    chats = ChatMessage.objects.filter(chatRoomId = 1).order_by("timestamp").values()
    print(chats)
    return Response({'data' : chats})