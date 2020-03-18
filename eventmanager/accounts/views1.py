from django.shortcuts import render
from .models import UserModel
from .serializers import AccountsSerializerPaid
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser

class UserViewSetPaid(viewsets.ModelViewSet):
    serializer_class = AccountsSerializerPaid
    queryset = UserModel.objects.all()
    permission_classes  = [permissions.AllowAny]
    authentication_classes = []
    parser_classes = [MultiPartParser]
