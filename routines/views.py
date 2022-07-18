from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from routines.models import Routine
from routines.serializers import RoutineSerializer


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_permissions(self):
        if self.action in ("destroy", "create", "update"):
            permission_classes = [IsAdminUser]
        elif self.action in ("list", "retrieve"):
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == 'retrieve':
            queryset = Routine.objects.all()
            user_id = self.request.query_params.get('user_id')
            if user_id is not None:
                queryset = queryset.filter(user_id=user_id)
            return queryset