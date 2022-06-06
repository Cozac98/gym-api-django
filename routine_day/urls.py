from typing import List
from django.urls import path

from .views import RoutineDayViewSet


urlpatterns = [
    path("", RoutineDayViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>/",
        RoutineDayViewSet.as_view(
            {"put": "update", "delete": "destroy", "get": "retrieve"}
        ),
    ),
]
