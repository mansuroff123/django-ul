from django.contrib import admin
from .models import Item

# Register your models here.

# admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') # Admin panelda ko'rsatiladigan ustunlar
    search_fields = ['name'] # Admin panelda search field yaratish
