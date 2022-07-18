from dataclasses import fields
from rest_framework import serializers

from exercise.serializers import ExerciseWithRelationSerializer

from .models import RoutineDayExercise



class RoutineDayExerciseSerializerWithRelationship(serializers.ModelSerializer):
    exercise = ExerciseWithRelationSerializer(read_only=True)

    class Meta:
        model = RoutineDayExercise
        fields = "__all__"


class RoutineDayExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDayExercise
        fields = "__all__"
