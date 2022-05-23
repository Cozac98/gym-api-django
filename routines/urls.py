from .views import ListCreateExercise, RetrieveUpdateDeleteExercise
from django.urls import path


urlpatterns = [
    path("", ListCreateExercise.as_view(), name="list-create-exercises"),
    path(
        "<int:pk>/",
        RetrieveUpdateDeleteExercise.as_view(),
        name="list-create-exercises",
    ),
]
