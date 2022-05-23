from django.db import models

# Create your models here.
class MuscleGroup(models.Model):
    name = models.CharField(max_length=30, null=False)
