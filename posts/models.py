from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Soln(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    explaination = models.CharField(max_length=3000)
    code = models.TextField(max_length=5000)
    posted_by = models.CharField(max_length=100)  # Name or username of the person who posted the code

    def __str__(self):
        return self.title 


from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
