from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify_token/", TokenVerifyView.as_view(), name="verify_token"),
    path("signup/", views.RegisterUserAPIView.as_view(), name="signup"),
    path("staff-signup/", views.RegisterStaffAPIView.as_view(), name="signup"),
    path('users/', views.GetUsersAPIView.as_view(), name="users"),
    path('me/', views.me),

]
