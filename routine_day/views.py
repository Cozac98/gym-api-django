from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from routine_day.models import RoutineDay
from .serializers import RoutineDaySerializerWithRelationship, RoutineDaySerializer

class RoutineDayViewSet(viewsets.ModelViewSet):
    queryset = RoutineDay.objects.all()
    serializer_class = RoutineDaySerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoutineDaySerializerWithRelationship
        return RoutineDaySerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
