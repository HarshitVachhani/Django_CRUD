from django.contrib import admin
from employee.models import Employee

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'e_name', 'e_designation', 'e_email', 'e_contact')
    
admin.site.register(Employee, EmpAdmin)