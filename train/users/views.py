from users.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
