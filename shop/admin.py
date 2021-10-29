from django.contrib import admin

# Register your models here.
from .models import Item, Images, CartItem

admin.site.register(Images)
admin.site.register(Item)
