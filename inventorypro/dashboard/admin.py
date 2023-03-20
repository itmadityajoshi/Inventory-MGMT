from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_header = 'VhatiInventory Dashboard'
admin.site.register(Product)