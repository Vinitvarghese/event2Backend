from django.db import models
from django.conf import settings
from contacts.models import Contacts

# Create your models here.
class UserModel(models.Model):
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

    user                =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    agreement_number    =   models.CharField(max_length=100)
    position            =   models.CharField(max_length=50)
    company             =   models.CharField(max_length=50)
    email_address       =   models.EmailField()
    phone_number        =   models.IntegerField()
    country             =   models.CharField(max_length=50)
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
    # def __str__(self):
    #     return self.user