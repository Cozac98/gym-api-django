from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import RoutineDayExercise
from .serializers import RoutineDayExerciseSerializerWithRelationship, RoutineDayExerciseSerializer

class RoutineDayExerciseViewSet(viewsets.ModelViewSet):
    queryset = RoutineDayExercise.objects.all()
    serializer_class = RoutineDayExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["routine_day"]


    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoutineDayExerciseSerializerWithRelationship
        return RoutineDayExerciseSerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]