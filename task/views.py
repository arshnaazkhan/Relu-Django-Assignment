from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import permissions

from .serializers import UserRegistrationSerializer, StudentSerializer, PasswordResetSerializer
from .permission import SuperAdminPermission, TeacherPermission, StudentPermission


User = get_user_model()

"""This View can create and retrun list of all User instance"""

class UserRegistrationView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SuperAdminPermission]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


"""This View can create and retrun list of Student type User instance"""

class StudentListView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TeacherPermission]
    serializer_class = StudentSerializer
    queryset = User.objects.filter(groups__name='Student')


"""This View can  retrun list of a single User instance"""

class StudentView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, StudentPermission]
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user


"""This View can create new password for a User instance"""

class PasswordResetView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
