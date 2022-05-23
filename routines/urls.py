from .views import ListCreateRoutine, RetrieveUpdateDeleteRoutine
from django.urls import path


urlpatterns = [
    path("", ListCreateRoutine.as_view(), name="list-create-routines"),
    path(
        "<int:pk>/",
        RetrieveUpdateDeleteRoutine.as_view(),
        name="retrieve-update-delete-routine",
    ),
]
