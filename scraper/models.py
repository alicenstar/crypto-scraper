from django.db import models

# Create your models here.
class Article(models.Model):
    header = models.CharField(max_length=200)
    # image = models.CharField(max_length=200)
    # content = models.TextField(blank=True)