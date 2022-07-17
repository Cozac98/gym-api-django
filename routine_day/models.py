from pickle import FALSE
from django.db import models
from routines.models import Routine
from exercise.models import Exercise

# Create your models here.
class RoutineDay(models.Model):
    number_day = models.IntegerField(null=False)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_days')
    exercises = models.ManyToManyField(Exercise)
