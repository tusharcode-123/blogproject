from django.db import models
from account.models import Register

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='img1.jpg')
    author = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    favourties = models.ManyToManyField(Register,related_name='favourties',default=None,blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Register,related_name="person", on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='avatar.png')
    name = models.CharField(max_length=342)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)