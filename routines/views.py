from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from routines.models import Routine
from routines.serializers import RoutineSerializer

# Create your views here.
class ListCreateRoutine(ListCreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class RetrieveUpdateDeleteRoutine(RetrieveUpdateDestroyAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
