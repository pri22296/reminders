from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length = 140)
    detail = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    date = models.DateField()

    def __str__(self):
        return self.title
