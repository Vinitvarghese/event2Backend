from rest_framework import serializers
#from .models import UserModel
from contacts.serializers import ContactSerializer
from contacts.models import Contacts
from accounts.models import UserModel
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


class AccountsSerializerPaid(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields =[
            'id',
            'username',
            "first_name",
            "last_name",
            'password',
            "email",
            'phone_number',
            'position',
            'company',            
            'country',
            'company_type',
             "user_type",
            'agreement_number',
            'profile_pic',
            'summary',
            'terms']
        read_only = ['id']
    def create(self,validated_data):
        agreement_num=validated_data["agreement_number"]
        if(Contacts.objects.filter(unique_number=agreement_num).first() and Contacts.objects.filter(is_valid=True)):
            Contacts.objects.filter(unique_number=agreement_num).update(is_valid=False)
            user=UserModel.objects.create(password = make_password(validated_data['password']),**validated_data)
            return user
        else:
           raise serializers.ValidationError({"response":"Wrong account number"})
        return user

    def update(self, instance, validated_data):
        instance.first_name= validated_data.get('first_name',instance.first_name)
        instance.last_name= validated_data.get('last_name',instance.last_name)
        instance.username= validated_data.get('username',instance.username)
        instance.position = validated_data.get('position', instance.position)
        instance.company = validated_data.get('company', instance.company)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.country = validated_data.get('country', instance.country)
        instance.company_type = validated_data.get('company_type', instance.company_type)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.agreement_number = validated_data.get('agreement_number', instance.agreement_number)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()
        
        return instance