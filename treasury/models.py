from django.db import models

# Create your models here.
class Creditor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    contact_person = models.CharField(max_length=200)

class Debt(models.Model):
    name = models.CharField(max_length=200)
    occurance = models.DurationField
    amount = models.DecimalField(max_digits=20,decimal_places=2)
