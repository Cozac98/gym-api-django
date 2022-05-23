from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import MuscleGroup
from .serializers import MuscleGroupSerializer

# Create your views here.
class ListCreateMuscleGroup(ListCreateAPIView):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


class RetrieveUpdateDeleteMuscleGroup(RetrieveUpdateDestroyAPIView):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
