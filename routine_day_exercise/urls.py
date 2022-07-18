from typing import List
from django.urls import path

from .views import RoutineDayExerciseViewSet


urlpatterns = [
    path("", RoutineDayExerciseViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        RoutineDayExerciseViewSet.as_view(
            {"put": "update", "delete": "destroy", "get": "retrieve"}
        ),
    ),
]
