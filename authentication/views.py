from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method="POST", request_body=UserSerializer)
@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)
