from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import UserCreds
from .serializers import UserCredsSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# User Registration
class RegisterAPIView(generics.CreateAPIView):
    queryset = UserCreds.objects.all()
    serializer_class = UserCredsSerializer
    permission_classes = [AllowAny]

# User Login
class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description='Token',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'token': openapi.Schema(type=openapi.TYPE_STRING)}
                )
            ),
            400: 'Bad Request',
            401: 'Unauthorized'
        },
        operation_summary='User Login',
        operation_description='Logs in a user and returns an authentication token.'
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         username = serializer.validated_data['username']
    #         password = serializer.validated_data['password']
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             token, created = Token.objects.get_or_create(user=user)
    #             return Response({'token': token.key}, status=status.HTTP_200_OK)
    #         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)