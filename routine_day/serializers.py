from dataclasses import fields
from rest_framework import serializers

from .models import RoutineDay
from routines.serializers import RoutineSerializer


class RoutineDaySerializerWithRelationship(serializers.ModelSerializer):
    routine = RoutineSerializer(read_only=True)

    class Meta:
        model = RoutineDay
        fields = "__all__"


class RoutineDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = "__all__"
