from django.shortcuts import render
from .models import UserModel
from .serializers import AccountsSerializerPaid, AccountsSerializerGuest
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser

# Create your views here.



class UserViewSetPaid(viewsets.ModelViewSet):
    serializer_class = AccountsSerializerPaid
    queryset = UserModel.objects.all()
    permission_classes  = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = [MultiPartParser]

class UserViewSetGuest(viewsets.ModelViewSet):
    serializer_class = AccountsSerializerGuest
    queryset = UserModel.objects.all()
    permission_classes  = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = [MultiPartParser]


    # def post(self, request):
    #     print("Hello This ",request.data)

# class UserList(viewsets.ModelViewSet):
#     serializer_class = UserPerfect
#     queryset = UserNew.objects.all()
#     permission_classes  = [permissions.AllowAny]
#     authentication_classes = []
    # parser_classes = [MultiPartParser]
