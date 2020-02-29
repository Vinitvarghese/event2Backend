from django.shortcuts import render
from .models import UserModel 
from .serializers import AccountsSerializer
from rest_framework import viewsets, permissions
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = AccountsSerializer
    queryset = UserModel.objects.all()
    permission_classes  = [permissions.AllowAny]
    authentication_classes = []
