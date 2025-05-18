from django.contrib import admin
from . models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','position','description','address','phone','date')
    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','images','date_added')
    
    
    list_filter=('name','date_added')


admin.site.register(Student,StudentAdmin)
admin.site.register(Product,ProductAdmin)
