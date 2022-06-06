from django.urls import path
from .views import MuscleGroupViewSet


urlpatterns = [
    path("", MuscleGroupViewSet.as_view({"get": "list", "post": "create"}), name="list-create-muscle-groups"),
    path(
        "<int:pk>/",
        MuscleGroupViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="list-create-muscle-groups",
    ),
]
