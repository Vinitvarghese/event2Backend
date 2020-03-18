from rest_framework import serializers
from .models import UserModel
from contacts.serializers import ContactSerializer
from contacts.models import Contacts
from accounts.models import UserModel
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from datetime import timedelta,datetime
from django.utils.text import gettext_lazy as _
User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    model = UserModel

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



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

class AccountsSerializerGuest(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            "username",
            "first_name",
            "last_name",
            'password',
            "email",
            'phone_number',
            'position',
            'company',            
            'country',
            'company_type',
            'profile_pic',
            'summary',
            'terms'
        ]
        read_only = ['id']

    def create(self, validated_data):
        user = UserModel(username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],
                    email=validated_data['email'],phone_number=validated_data['phone_number'],position=validated_data['position'],company=validated_data['company'],country=validated_data['country'],
                    company_type=validated_data['company_type'],profile_pic=validated_data['profile_pic'],summary=validated_data['summary'],terms=validated_data['terms'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        #return UserModel.objects.create(**validated_data)
    def update(self,instance,validated_data):
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
            user = UserModel(username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],
                    email=validated_data['email'],phone_number=validated_data['phone_number'],position=validated_data['position'],company=validated_data['company'],country=validated_data['country'],
                    company_type=validated_data['company_type'],user_type=validated_data['uesr_type'],agreement_number=validated_data['agreement_number'],profile_pic=validated_data['profile_pic'],summary=validated_data['summary'],terms=validated_data['terms'])
            user.set_password(validated_data['password'])
            user.save()

            #user=UserModel.objects.create(**validated_data)
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
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        '''data['groups'] = self.user.date_joined #self.user.groups.values_list('name', flat=True)
        data['change_model']=EmpAddress.objects.filter(employee_street="Jakksandra").first().employee_home'''
        return data
class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
 
        return attrs

    def save(self, **kwargs):
        try:
            print(self.token)
            test = RefreshToken(self.token).access_token
            print(test)
            test.set_exp(datetime.now())
            RefreshToken(self.token).blacklist()
            return Response("Successfully logged out")
            
            
        except TokenError:
            self.fail('bad_token')
'''class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])

        return {}'''
    
    