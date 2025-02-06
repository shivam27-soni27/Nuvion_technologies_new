from django.db import models

# Create your models here.
# yourapp/models.py
from django.db import models

class Workwithus(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    company = models.CharField(max_length=100,default='')
    field_of_work = models.CharField(max_length=500,default='')
    desc = models.CharField(max_length=500,default='')
    webap=models.BooleanField(default=False)
    app=models.BooleanField(default=False)

    def __str__(self):
        return self.name
