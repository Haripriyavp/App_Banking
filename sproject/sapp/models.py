from django.db import models

# Create your models here.
class Check(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    district = models.CharField( max_length=100, null=True)
    branch = models.CharField(max_length=50, null=True)
    account_type = models.CharField(null=True, max_length=50)
    materials_provided = models.CharField(max_length=50)