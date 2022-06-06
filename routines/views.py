from rest_framework import viewsets

from routines.models import Routine
from routines.serializers import RoutineSerializer

# Create your views here.
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
