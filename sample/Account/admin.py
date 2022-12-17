from django.contrib import admin
from .models import Contact,Course,Staff


# Register your models here.
class Customerdetails(admin.ModelAdmin):
    list_display=('name','phone','email')
admin.site.register(Contact,Customerdetails)
admin.site.register(Course)
admin.site.register(Staff)