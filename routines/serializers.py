from rest_framework import serializers

from routines.models import Routine
from muscle_groups.serializers import MuscleGroupSerializer


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"
