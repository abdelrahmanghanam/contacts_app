from django.db import models
from django.db import models

#simple we do not need to have more than two tables. It is a simple case

#first model is contact
class Contact(models.Model):
    #we don't need to implement id field it is there by default.
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta:
        db_table = "Contact"

#the second model is phone number which has many-to-one relationship with contact
class PhoneNumber(models.Model):
    #we don't need to implement id field it is there by default.
    country_code = models.CharField(max_length=5)
    #we need the phone number to be unique to avoid duplicates
    phone_number = models.CharField(max_length=15,unique=True)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    class Meta:
        db_table = "PhoneNumber"
