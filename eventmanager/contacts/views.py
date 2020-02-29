from django.shortcuts import render
from .models import Contacts 
from .serializers import ContactSerializer
from leads.views import LeadsList
from rest_framework import viewsets
import json
# Create your views here.



class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()    
        



