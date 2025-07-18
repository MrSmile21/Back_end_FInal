from django.db import models
from departments.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_joined = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str(self):
        return self.name