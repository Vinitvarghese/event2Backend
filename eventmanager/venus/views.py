from django.shortcuts import render
from .models import Venus 
from .serializers import VenuSerializer
from rest_framework import viewsets

# Create your views here.



class VenuViewSet(viewsets.ModelViewSet):
    serializer_class = VenuSerializer
    queryset = Venus.objects.all()