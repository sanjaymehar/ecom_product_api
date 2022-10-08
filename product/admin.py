from django.contrib import admin

from product.models import Product

# For showing models in admin panel
admin.site.register(Product)