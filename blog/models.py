from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Hayden Decker")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #This is a function but we omitt the parentheses 
                                                             #as we want to pass the actual function as the default value.
    def __str__(self):
        return self.title

