from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import MuscleGroup
from .serializers import MuscleGroupSerializer

# Create your views here.
class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
