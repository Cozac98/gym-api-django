from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer, ExerciseWithRelationSerializer

# Create your views here.
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["muscle_group"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ExerciseWithRelationSerializer
        return ExerciseSerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]