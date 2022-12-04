from django.db import models

from muscle_groups.models import MuscleGroup

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, null=False)
