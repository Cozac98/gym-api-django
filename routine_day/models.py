from pickle import FALSE
from django.db import models
from routines.models import Routine

# Create your models here.
class RoutineDay(models.Model):
    number_day = models.IntegerField(null=False)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
