from django.db import models
from datetime import datetime
# Create your models here.


class Profile(models.Model):
    genderChoices=[
        ('male','male'),
        ('female','female')
    ]
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices= genderChoices)
    
    def __str__(self):
        return self.name

class Visits(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to='photos/%y/%m/%d')
    description=models.TextField(null=True,blank=True)
    dateCreated=models.DateTimeField(default=datetime.now)
    profileID=models.ForeignKey(Profile , on_delete=models.CASCADE)   
    
         
    
    
    