from django.db import models

# Create your models here.

class Employee(models.Model):
    
    e_id = models.CharField(max_length=20)
    e_name = models.CharField(max_length=60)
    e_designation = models.CharField(max_length=100)
    e_email = models.EmailField()
    e_contact = models.CharField(max_length=10)
    
    class Meta:
        db_table = "employee"