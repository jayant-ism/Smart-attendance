from django.db import models


class student(models.Model):
    
  
    phone = models.TextField()
    name = models.TextField()
    reg = models.TextField() 
    attend = models.TextField()
    img = models.TextField(default="static/current/dist/img/user1-128x128.jpg")
    



# Create your models here.
