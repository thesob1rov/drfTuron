from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import Student
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# @permission_classes([IsAuthenticated])
class UserCreate(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def post(self, request):
        current_user = request.user
        User = get_user_model()
        # User.objects.create_user(**request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            student = Student(user_id=user.pk)
            student.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
