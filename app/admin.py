from django.contrib import admin

# Register your models here.
from .models import ItemModel

admin.site.register(ItemModel)