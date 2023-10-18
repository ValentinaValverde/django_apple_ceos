from django.db import models

# Create your models here.
class CeosUpdate(models.Model):
    name = models.TextField(max_length=100)
    slug = models.TextField(max_length=100)
    first_year_active = models.IntegerField()
