from django.contrib import admin


# Register your models here.
from logic.models import Brand, Product

admin.site.register(Brand)
admin.site.register(Product)
