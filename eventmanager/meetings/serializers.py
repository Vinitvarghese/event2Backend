from rest_framework import serializers
from .models import Meeting
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]

class MeetingFromSerializer(serializers.ModelSerializer):
    meeting_with = UserSerializer(read_only=True)
    meeting_from = UserSerializer(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'id',
            'start_time',
            'end_time',
            'meeting_with',
            "meeting_from",
            'meeting_description'
        ]
        read_only = ['id']

class MeetingToSerializer(serializers.ModelSerializer):
    meeting_with = UserSerializer(read_only=True)
    meeting_from = UserSerializer(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'id',
            'start_time',
            'end_time',
            'meeting_with',
            "meeting_from",
            "acceptance",
            'meeting_description'
        ]
        read_only = ['id']

class MeetingSerializer(serializers.ModelSerializer):
    meeting_with = UserSerializer(read_only=True)
    # meeting_from = UserSerializer(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'id',
            'start_time',
            'end_time',
            'meeting_with',
            'acceptance',
            'meeting_description'
        ]
        read_only = ['id']
   


class MeetingFromCreateSerializer(serializers.ModelSerializer):
    meeting_with = UserSerializer
    class Meta:
        model = Meeting
        fields = [
            'id',
            'start_time',
            'end_time',
            'meeting_with',
            'meeting_description'
        ]
        read_only = ['id']

# class MeetingFromUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meeting
#         fields = [
#             'id',
#             'start_time',
#             'end_time',
#             'meeting_with',
#             'meeting_description'
#         ]
#         read_only = ['id']
