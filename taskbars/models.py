from django.db import models
from django.urls import reverse
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    completed = models.BooleanField(default = False)
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("taskbars:details",kwargs ={"id":self.id})