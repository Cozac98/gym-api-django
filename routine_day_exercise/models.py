from pickle import FALSE
from django.db import models
from routine_day.models import RoutineDay
from exercise.models import Exercise

# Create your models here.
class RoutineDayExercise(models.Model):
    reps = models.IntegerField(null=False)
    sets = models.IntegerField(null=False)
    routine_day = models.ForeignKey(RoutineDay, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
