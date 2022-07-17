from rest_framework import serializers

from routine_day.serializers import RoutineDaySerializerWithRelationship

from routines.models import Routine


class RoutineSerializer(serializers.ModelSerializer):
    routine_days = RoutineDaySerializerWithRelationship(read_only=True, many=True)
    class Meta:
        model = Routine
        fields = "__all__"
