from rest_framework import viewsets

from .models import MuscleGroup
from .serializers import MuscleGroupSerializer

# Create your views here.
class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer
