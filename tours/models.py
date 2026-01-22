from django.db import models
from django.utils.text import slugify

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration_days = models.PositiveIntegerField()
    price_usd = models.PositiveIntegerField()
    location = models.CharField(max_length=100, default='Kyzyl Suu')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title