from django.db import models

# Create your models here.

def upload_files(instance,filename):
    return "status/{filename}".format(filename=filename)

class Venus(models.Model):
    venue_title     =   models.CharField(max_length=100)
    region          =   models.CharField(max_length=30)
    event_date      =   models.DateField()
    description     =   models.CharField(max_length=300)
    co_ordinate_x   =   models.CharField(max_length=200)
    co_ordinate_y   =   models.CharField(max_length=200)
    venu_image      =   models.ImageField(upload_to=upload_files, null=True, blank=True)

    def __str__(self):
        return self.venue_title               
    