from dataclasses import fields
from rest_framework import serializers

from routine_day_exercise.serializers import RoutineDayExerciseSerializerWithRelationship

from .models import RoutineDay



class RoutineDaySerializerWithRelationship(serializers.ModelSerializer):
    exercises = RoutineDayExerciseSerializerWithRelationship(read_only=True, many=True)

    class Meta:
        model = RoutineDay
        fields = "__all__"


class RoutineDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = "__all__"
