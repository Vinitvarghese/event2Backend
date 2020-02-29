from django.db import models

# Create your models here.
class Leads(models.Model):
    company_name    =   models.CharField(max_length=100)
    fullname        =   models.CharField(max_length=100)
    position        =   models.CharField(max_length=100)
    email           =   models.EmailField()
    tin_number      =   models.IntegerField()

    def __str__(self):
        return self.fullname