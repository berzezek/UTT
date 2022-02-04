from calendar import month, month_name
from operator import mod
from django.db import models


class Couch(models.Model):
    name = models.CharField(max_length=255)
    couch_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    tariff = models.IntegerField(null=True)
    couch = models.ForeignKey(Couch, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, blank=True)
    customer_description = models.TextField(blank=True)
    created_by = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

MONTH_NAME = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
MONTH = [(x, MONTH_NAME[x - 1]) for x in range(1, 13)]

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    value_of_payment = models.FloatField()
    date_of_payment = models.DateField(auto_now_add=True, blank=True)
    month_is_paid = models.IntegerField(choices=MONTH, blank=True)
    payment_description = models.TextField(blank=True)

