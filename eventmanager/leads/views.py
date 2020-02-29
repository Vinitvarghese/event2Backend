from django.shortcuts import render
from .models import Leads 
from .serializers import LeadSerializer
from rest_framework import viewsets, permissions

# Create your views here.

class LeadsList(viewsets.ModelViewSet):
    serializer_class        =       LeadSerializer
    queryset                =       Leads.objects.all()
    permission_classes      =       [permissions.AllowAny]
    authentication_classes  =       [] 
    
    


