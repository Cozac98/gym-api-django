from rest_framework import serializers

from routine_day.serializers import RoutineDaySerializerWithRelationship

from routines.models import Routine


class RoutineWithRelationSerializer(serializers.ModelSerializer):
    routine_days = RoutineDaySerializerWithRelationship(read_only=True, many=True)
    class Meta:
        model = Routine
        fields = "__all__"

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"

class QuerySerializer(serializers.Serializer):
    user_id = serializers.CharField()