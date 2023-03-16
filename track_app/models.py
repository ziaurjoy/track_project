from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name


class Devices(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True,null=True)

    def __str__(self):
        return self.name


class Employees(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

status = (
    ('Fresh Condition', 'Fresh Condition'),
    ('Not Fresh Condition', 'Not Fresh Condition')
)

class Tracks(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, blank=True,null=True)
    device = models.ForeignKey(Devices, on_delete=models.SET_NULL, blank=True,null=True)
    checked_out = models.DateTimeField(auto_now_add=True)
    checked_in = models.DateField()
    return_date = models.DateTimeField(blank=True, null=True)
    checked_out_status = models.CharField(choices=status, max_length=30)
    return_status = models.CharField(choices=status, max_length=30)
    
    def __str__(self):
        return self.employee.name

    