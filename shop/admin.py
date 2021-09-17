from django.contrib import admin
from . models import *
# Register your models here.


class categadmin(admin.ModelAdmin):
    # field slug and name same
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,categadmin)

class prodAdmin(admin.ModelAdmin):
    # its display firstly in admin panel
    list_display=['name','slug','price','stock','img','available','category']
    # not best option for name and slug change its edit directly in admin view products
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}

admin.site.register(products,prodAdmin)