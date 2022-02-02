from django.forms import ModelForm, formset_factory
from .models import Customer, Couch, Payment
from django import forms


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'couch', 'tariff', 'age', 'phone', 'customer_description', 'is_active')


class CouchForm(ModelForm):

    class Meta:
        model = Couch
        fields = '__all__'


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

