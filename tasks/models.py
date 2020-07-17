from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')






