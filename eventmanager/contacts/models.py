from django.db import models
from leads.models import Leads
# Create your models here.

class Contacts(models.Model):
    YES             =   'Yes'
    NO              =   'No'
    PAID_OPTIONS    = [ 
                        (YES,'Yes'),
                        (NO,'No')
                    ]
    paid            =   models.CharField(
                            max_length=50,
                            choices=PAID_OPTIONS,
                            default=NO
                        )
    amount          =   models.IntegerField()
    unique_number   =   models.IntegerField(primary_key=True)
    is_valid        =   models. BooleanField(default=True)
    leads_data      =   models.ForeignKey(Leads,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.unique_number)