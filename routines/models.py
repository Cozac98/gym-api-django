from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


# Create your models here.
class Routine(models.Model):
    is_completed = models.BooleanField(default=False)
    objective = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
