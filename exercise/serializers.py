from rest_framework import serializers

from exercise.models import Exercise
from muscle_groups.serializers import MuscleGroupSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    muscle_group = MuscleGroupSerializer(read_only=True)

    class Meta:
        model = Exercise
        fields = ["id", "name", "description", "muscle_group"]


class ExercisePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
