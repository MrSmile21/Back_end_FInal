from django.db import models
from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateField()
    
    def __str__(Self):
        return f"{self.employee.name} - {self.review_date}"