from django.db import models

# Create your models here.
class User(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    profilepic=models.FileField(upload_to='media/',default="anonymous.jpg")
    def __str__(self):
        return self.fullname
