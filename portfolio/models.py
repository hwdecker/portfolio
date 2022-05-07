from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.CharField(max_length=128)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    link = models.CharField(default="github.com/hwdecker", max_length=128)
    image = models.ImageField(upload_to='project_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)

    #    img = Image.open(self.image.path)

    #    if img.height > 720 or img.width > 1280:
    #       output_size = (720, 1280)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})