from django import forms  
from employee.models import Employee  

class EmployeeForm(forms.ModelForm):  

    class Meta:  
        model = Employee  
        fields = ['e_id','e_name','e_designation','e_email','e_contact']