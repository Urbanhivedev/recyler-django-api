from django.db import models
import uuid
from django.db import models
from django.utils import timezone
# Create your models here.
# models.py


def generate_user_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique user id

def generate_school_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique school id

class MainUsers(models.Model):
    user_id =  models.CharField(max_length=255, blank=True)
    user_name = models.CharField(max_length=60, blank=True)
    full_name = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=60, blank=True)
    phone_number = models.CharField(max_length=60, blank=True)
    email= models.EmailField(max_length=60, blank=True)
    password = models.CharField(max_length=60, blank=True)
    balance = models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True)   #This means that the field is optional in all circumstances
    date_created = models.CharField(max_length=255, default=timezone.now, blank=True)

    def __str__(self):
        return "{} - {}".format(self.user_name, self.user_id)

    def save(self, *args, **kwargs):
        if len(self.user_id.strip(" "))==0:
            self.user_id = generate_user_id()

        super(MainUsers, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-date_created"]



class Schools(models.Model):
    school_id =  models.CharField(max_length=255, blank=True)
    school_name = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=60, blank=True)
    phone_number = models.CharField(max_length=60, blank=True)
    email= models.EmailField(max_length=60, blank=True)
    password = models.CharField(max_length=60, blank=True)    
    date_created = models.CharField( max_length=255,default=timezone.now, blank=True)

    def __str__(self):
        return "{} - {}".format(self.school_name, self.school_id)

    def save(self, *args, **kwargs):
        if len(self.school_id.strip(" "))==0:
            self.school_id = generate_school_id()

        super(Schools, self).save(*args, **kwargs) # Call the real   save() method
