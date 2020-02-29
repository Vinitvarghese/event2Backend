
from django.contrib import admin
from django.urls import path, include
from .views import (
    MeetingFromListAPIView, 
    MeetingToListAPIView, 
    MeetingFromUpdateAPIView, 
    MeetingToListAPIView,
    MeetingFromCreateAPIView
)

urlpatterns = [
    path('from/',MeetingFromListAPIView.as_view()),
    path('to/',MeetingToListAPIView.as_view()),
    path('from/create/',MeetingFromCreateAPIView.as_view()),
    path(r'from/<int:pk>/update_delete/',MeetingFromUpdateAPIView.as_view()),
]
