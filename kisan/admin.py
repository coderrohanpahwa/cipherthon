from django.contrib import admin
from .models import Thing,Contact,Detail_item,Address
# Register your models here.
@admin.register(Thing)
class abc(admin.ModelAdmin):
    list_display = ['name','desc','price','number']
@admin.register(Contact)
class xyz(admin.ModelAdmin):
    list_display = ['name','email','query']
@admin.register(Detail_item)
class abcde(admin.ModelAdmin):
    list_display = ['name','quantity','price','vege']
class hdhs(admin.ModelAdmin):
    list_display = ['name','mobile','address']