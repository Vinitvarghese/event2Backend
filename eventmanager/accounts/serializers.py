from rest_framework import serializers
from .models import UserModel
from contacts.serializers import ContactSerializer
from contacts.models import Contacts
from accounts.models import UserModel
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()




# class UserPerfect(serializers.ModelSerializer):
#     class Meta:
#         model = UserNew
#         fields = [
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'password'
#         ]
#         read_only = ['id']


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
            # 'user_type',
            # 'agreement_number',
            'profile_pic',
            'summary',
            'terms'
        ]
        read_only = ['id']
        extra_kwargs = {
            # "password":{"write_only":True},
            # "phone_number":{"write_only":True},
            # "position":{"write_only":True},
            # "company":{"write_only":True},
            # "country":{"write_only":True},
            # "company_type":{"write_only":True},
            # # "user_type":{"write_only":True},
            # # "agreement_number":{"write_only":True},
            # "summary":{"write_only":True},
            # "terms":{"write_only":True},
            # "username":{"write_only":True},
        }



    def create(self, validated_data):
        # agreement_no = validated_data['agreement_number']
        # phone_number = validated_data['phone_number']
        # contactValue = Contacts.objects.filter(unique_number=agreement_no).first()
        # print("Hello from 1992",validated_data)
        # if contactValue is not None : 
            # password = validated_data.pop('password') 
            # print("Hello from 1992",**validated_data) 
            # obj = UserModel(**validated_data) 
            # obj.set_password(password)
            
        return UserModel.objects.create(**validated_data)
        # else :
        #     return { "details" : "Agreement number is not correct."}

class AccountsSerializerPaid(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            "first_name",
            "username",
            "last_name",
            'password',
            "email",
            'phone_number',
            'position',
            'company',            
            'country',
            'company_type',
            'user_type',
            'agreement_number',
            'profile_pic',
            'summary',
            'terms'
        ]
        read_only = ['id']
        extra_kwargs = {
            "password":{"write_only":True},
            "phone_number":{"write_only":True},
            "position":{"write_only":True},
            "company":{"write_only":True},
            "country":{"write_only":True},
            "company_type":{"write_only":True},
            "user_type":{"write_only":True},
            "agreement_number":{"write_only":True},
            "summary":{"write_only":True},
            "terms":{"write_only":True},
            "username":{"write_only":True},
        }



    def validate_agreement_number(self,agreement_number):
        print("Self data hello",agreement_number)
        contactValues = self.context.get("exclude_agreement_number_list", [])
        # contactValue = Contacts.objects.filter(unique_number=int(agreement_number)).first()
        if agreement_number in contactValues:
            print("HRellooolololl ......")
            raise serializers.ValidationError("We cannot send an email to this user")
        
        # if contactValue is None
        return Response({ "status" : "none" })

    def create(self, validated_data):
        agreement_no = validated_data['agreement_number']
        print("Hello uhij",agreement_no)
        # phone_number = validated_data['phone_number']
        contactValue = Contacts.objects.filter(unique_number=agreement_no).first()
        # print("Hello from 1992",validated_data)
        print("I am success bro......",contactValue)
        if contactValue is not None : 
            print("I am success bro 45......")
            return UserModel.objects.create(**validated_data)
        return { "status" : "none" }
            # password = validated_data.pop('password') 
            # print("Hello from 1992",**validated_data) 
            # obj = UserModel(**validated_data) 
            # obj.set_password(password)
        # data = '<html><body><h1>Hello, world</h1></body></html>'
        

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