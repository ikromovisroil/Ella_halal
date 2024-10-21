from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'summa', 'action_summa', 'status',)
    list_filter = ('category', 'status', 'action',)
    search_fields = ('name',)
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tel',)
    search_fields = ('full_name',)
