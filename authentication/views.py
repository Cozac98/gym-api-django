from rest_framework import generics, response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import StaffSerializer, UserSerializer

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = UserSerializer

class RegisterStaffAPIView(generics.CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = StaffSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    return response.Response(UserSerializer(request.user).data, 200)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def users(request):
    return response.Response(UserSerializer(request.user).data, 200)

class GetUsersAPIView(generics.ListAPIView):
  queryset = User.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = UserSerializer