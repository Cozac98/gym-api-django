from django.conf import settings
from django.db import models

# Create your models here.
class Routine(models.Model):
    is_completed = models.BooleanField(default=False)
    objective = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
