from django.db import models
from datetime import datetime
# Create your models here.


class Profile(models.Model):
    genderCoices=[
        ('male','male'),
        ('female','female')
    ]
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,null=True,blank=True,choices= genderCoices)
    
    def __str__(self):
        return self.name

class Visits(models.Model):
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    description=models.TextField()
    dateCreated=models.DateTimeField(default=datetime.now)
    profileID=models.ForeignKey(Profile , on_delete=models.CASCADE)        