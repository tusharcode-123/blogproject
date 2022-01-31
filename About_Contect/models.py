from django.db import models

# Create your models here.
class About(models.Model):
    Name = models.CharField(max_length=300)
    Discription = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='about/%Y/%m/%d/',default='avatar.png')


class Contect(models.Model):
    Name = models.CharField(max_length=300)
    Email = models.EmailField()
    Phone = models.CharField(max_length=10)
    Message = models.TextField()
