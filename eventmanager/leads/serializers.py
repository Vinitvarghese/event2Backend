from rest_framework import serializers
from .models import Leads


class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = [
            'id',
            'company_name',
            'fullname',
            'position',
            'email',
            'tin_number'
        ]

class LeadWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = [
            'id'
        ]
        extra_kwargs = {'id': {'read_only': False}}
