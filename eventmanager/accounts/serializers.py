from rest_framework import serializers
from .models import UserModel
from contacts.serializers import ContactSerializer
from contacts.models import Contacts
from accounts.models import UserModel
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
            'password'
        ]
        read_only = ['id']

class AccountsSerializer(serializers.ModelSerializer):
    user =  UserSerializer(required=True)
    class Meta:
        model = UserModel
        fields = [
            'id',
            'user',
            'position',
            'company',
            'email_address',
            'phone_number',
            'country',
            'company_type',
            'user_type',
            'agreement_number',
            'profile_pic',
            'summary',
            'terms'
        ]
        read_only = ['id']

    def create(self, validated_data):
        agreement_no = validated_data['agreement_number']
        print("Hello Sir",validated_data)
        data = validated_data.pop('user')
        contactValue = Contacts.objects.filter(unique_number=agreement_no).first()

        if contactValue is not None :
            user_obj = User(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password']
            )
            user_obj.set_password(data['password'])            
            new_u = user_obj.save()
            new_user_obj = User.objects.filter(id=user_obj.id).first()
            print("Hello Sir its me",user_obj.id)
            user_data = UserModel.objects.create(user=new_user_obj, **validated_data)
            return user_data
        else :
            return { "details" : "Agreement number is not correct."}

    # def update(self, instance, validated_data):
    #     print("Self data",self.data['user']['id'])
    #     print("validated data",validated_data.get('user', instance.user))
    #     userObj = User.objects.filter(id=self.data['user']['id']).first()
        
    #     userObj.username = validated_data['user']['username']
    #     userObj.first_name = validated_data['user']['first_name']
    #     userObj.last_name = validated_data['user']['last_name']
    #     userObj.save()

    #     instance.position = validated_data.get('position', instance.position)
    #     instance.company = validated_data.get('company', instance.company)
    #     instance.email_address = validated_data.get('email_address', instance.email_address)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.company_type = validated_data.get('company_type', instance.company_type)
    #     instance.user_type = validated_data.get('user_type', instance.user_type)
    #     instance.agreement_number = validated_data.get('agreement_number', instance.agreement_number)
    #     instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
    #     instance.summary = validated_data.get('summary', instance.summary)
    #     instance.save()
        
    #     return instance