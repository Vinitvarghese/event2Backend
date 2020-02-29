from rest_framework import serializers
from .models import Contacts
from leads.models import Leads
from leads.serializers import LeadWriteSerializer


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    leads_data  = LeadWriteSerializer()
    class Meta:
        model = Contacts
        fields = [
            # 'id',
            'paid',
            'amount',
            'unique_number',
            'leads_data',
        ]

    def create(self, validated_data):
        _id = validated_data['leads_data']['id']
        lead_data = Leads.objects.get(id=_id)    
        lead_obj = validated_data.pop('leads_data')
        createdObj = Contacts.objects.create(
            leads_data=lead_data,
            **validated_data
        )

        return createdObj
        

        
