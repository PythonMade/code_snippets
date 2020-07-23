from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_archived = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title