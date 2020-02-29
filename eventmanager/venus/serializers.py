from rest_framework import serializers
from .models import Venus


class VenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venus
        fields = [
            'id',
            'venue_title',
            'region',
            'event_date',
            'description',
            'co_ordinate_x',
            'co_ordinate_y',
            'venu_image'
        ]
        read_only = ['id']
