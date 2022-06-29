from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from routine_day.models import RoutineDay
from .serializers import RoutineDaySerializerWithRelationship, RoutineDaySerializer

# Create your views here.
class RoutineDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineDay.objects.all()
    serializer_class = RoutineDaySerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoutineDaySerializerWithRelationship
        return RoutineDaySerializer
