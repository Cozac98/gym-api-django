from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from routines.models import Routine
from routines.serializers import RoutineSerializer

# Create your views here.
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]