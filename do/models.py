from django.db import models

class do(models.Model):
    start_date_time = models.DateTimeField(blank=True)
    description = models.TextField()
    end_date_time = models.DateTimeField(blank=True)
    completed = models.BooleanField(default=False)
