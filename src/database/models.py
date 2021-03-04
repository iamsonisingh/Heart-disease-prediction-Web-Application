from django.db import models

# Create your models here.
class userInfo(models.Model):
    age=models.IntegerField()
    sex=models.CharField(max_length=10) # max_length = required
    cp=models.TextField()
    trestbps=models.IntegerField()
    cholestrol=models.IntegerField()
    fbs=models.BooleanField()
    restecg=models.TextField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.CharField(max_length=50)
    slope=models.CharField(max_length=50)
    ca=models.IntegerField()
    thal=models.CharField(max_length=50)

class user(models.Model):
    username = models.TextField()
    password = models.TextField()