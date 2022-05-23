from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer, ExerciseWithRelationSerializer

# Create your views here.
class ListCreateExercise(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class RetrieveUpdateDeleteExercise(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseWithRelationSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return ExerciseSerializer
        return self.serializer_class

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
