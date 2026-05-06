from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.course.models import Group


class GroupListSeralizer(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"


class GroupCreateSeralizer(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"






