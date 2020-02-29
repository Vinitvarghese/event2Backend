from django.shortcuts import render
from .models import Meeting 
from .serializers import MeetingSerializer, MeetingFromCreateSerializer, MeetingFromSerializer, MeetingToSerializer
from rest_framework import viewsets, generics, mixins
from rest_framework import permissions
from eventmanager.restconf.permission import IsOwnerOrReadOnly
# Create your views here.


class MeetingFromListAPIView(generics.ListAPIView):
    queryset                =   Meeting.objects.all()
    serializer_class        =   MeetingFromSerializer
    permission_classes      =   [permissions.AllowAny]
    authentication_classes  =   []

class MeetingToListAPIView(generics.ListAPIView):
    queryset                =   Meeting.objects.all()
    serializer_class        =   MeetingToSerializer
    permission_classes      =   [permissions.AllowAny]
    authentication_classes  =   []

class MeetingFromCreateAPIView(generics.CreateAPIView):
    queryset                =   Meeting.objects.all()
    serializer_class        =   MeetingSerializer
    #permission_class       =   [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes      =   [permissions.AllowAny]
    authentication_classes  =   []

    def perform_create(self, serializer):
        return serializer.save(meeting_from=self.request.user)


# class MeetingFromListAPIView(generics.ListCreateAPIView):
#     queryset                =   Meeting.objects.all()
#     serializer_class        =   MeetingSerializer
#     #permission_class       =   [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     permission_classes      =   [permissions.AllowAny]
#     authentication_classes  =   []

#     def perform_create(self, serializer):
#         return serializer.save(meeting_from=self.request.user)

# class MeetingFromCreateAPIView(
#         generics.CreateAPIView
#     ):
#     queryset                =   Meeting.objects.all()
#     serializer_class        =   MeetingFromCreateSerializer
#     #permission_class       =   [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     permission_classes      =   [permissions.AllowAny]
#     authentication_classes  =   []

class MeetingFromUpdateAPIView(
        generics.RetrieveUpdateDestroyAPIView
    ):
    queryset                =   Meeting.objects.all()
    serializer_class        =   MeetingFromCreateSerializer
    #permission_class       =   [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes      =   [permissions.AllowAny]
    authentication_classes  =   []

    def perform_update(self, serializer):
        return serializer.save(meeting_from=self.request.user)

# class MeetingToListAPIView(generics.ListAPIView):
#     queryset                =   Meeting.objects.all()
#     serializer_class        =   MeetingSerializer
#     #permission_class       =   [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     permission_classes      =   [permissions.AllowAny]
#     authentication_classes  =   []
