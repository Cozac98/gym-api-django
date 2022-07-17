from dataclasses import fields
from rest_framework import serializers

from exercise.serializers import ExerciseWithRelationSerializer

from .models import RoutineDay



class RoutineDaySerializerWithRelationship(serializers.ModelSerializer):
    exercises = ExerciseWithRelationSerializer(read_only=True, many=True)

    class Meta:
        model = RoutineDay
        fields = "__all__"


class RoutineDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = "__all__"
