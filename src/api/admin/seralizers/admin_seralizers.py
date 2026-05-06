from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.users.models import User


class UserListSeralizer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSeralizer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"








