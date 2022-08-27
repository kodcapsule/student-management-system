from django.db import models

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)    
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=500)

#     # def __str__  (self):
#     #     self.first_name

