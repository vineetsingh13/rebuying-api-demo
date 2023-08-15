from django.contrib import admin

# Register your models here.
from .models import AccountCreationDetails, ProductDetails
admin.site.register(AccountCreationDetails)
admin.site.register(ProductDetails)
