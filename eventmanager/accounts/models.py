from django.db import models
from django.conf import settings
from contacts.models import Contacts
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    SHIP_OWNER          =   'SO'
    SHIPYARDS           =   'SY'
    PORTS               =   'PR'
    EQUIPMENTS_PROVIDER =   'EP'
    YES                 =   'Yes'
    NO                  =   'No'
    TERMS_OPTION        =   [ (YES,'Yes'),(NO,'No') ]
    COMPANY_TYPE        =   [
                                (SHIP_OWNER,'Ship-owners'),
                                (SHIPYARDS,'Shipyards'),
                                (PORTS,'Ports'),
                                (EQUIPMENTS_PROVIDER,'Eqipments Provider')
                            ]

    PANELIST            =   'Panelist'
    DELEGATE            =   'Delegate'
    EXHIBITOR           =   'Exhibitor'
    SPEAKER             =   'Speaker'
    USER_TYPE           =   [
                                (PANELIST,'Panelist'),
                                (DELEGATE,'Delegate'),
                                (EXHIBITOR,'Exhibitor'),
                                (SPEAKER,'Speaker')
                            ]
                            
    position            =   models.CharField(max_length=50)
    company             =   models.CharField(max_length=50)
    email_address       =   models.EmailField()
    phone_number        =   models.CharField(max_length=10,null=True)
    country             =   models.CharField(max_length=50)
    agreement_number    =   models.IntegerField(null=True)
    company_type        =   models.CharField(
                                max_length=50,
                                choices=COMPANY_TYPE,
                                default=SHIP_OWNER
                                )
    user_type           =   models.CharField(
                                max_length=50,
                                choices=USER_TYPE,
                                default=PANELIST    
                            )
    profile_pic         =   models.ImageField(null=True)
    summary             =   models.CharField(max_length=100)
    description         =   models.CharField(max_length=100)
    terms               =   models.CharField(
                                max_length=3,
                                choices=TERMS_OPTION,
                                default=YES
                            )
    def __str__(self):
        return self.email_address


# class UserNew(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)