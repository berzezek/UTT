from django.contrib import admin
from .models import Couch, Payment, Customer


admin.site.register(Couch)
admin.site.register(Payment)
admin.site.register(Customer)
