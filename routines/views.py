from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from routines.models import Routine
from routines.serializers import RoutineSerializer, RoutineWithRelationSerializer


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoutineWithRelationSerializer
        return RoutineSerializer