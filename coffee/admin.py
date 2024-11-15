from django.contrib import admin
from .models import Coffee, Cart
# Register your models here.

class CoffeeAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'quantity', 'image', 'description', 'origin', 'flavor_profile')

admin.site.register(Coffee, CoffeeAdmin )
admin.site.register(Cart)