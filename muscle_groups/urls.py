from .views import ListCreateMuscleGroup, RetrieveUpdateDeleteMuscleGroup
from django.urls import path


urlpatterns = [
    path("", ListCreateMuscleGroup.as_view(), name="list-create-muscle-groups"),
    path(
        "<int:pk>/",
        RetrieveUpdateDeleteMuscleGroup.as_view(),
        name="list-create-muscle-groups",
    ),
]
