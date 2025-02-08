from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    publish_date = models.DateField()
    status = models.CharField
