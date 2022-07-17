from rest_framework import generics, response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

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