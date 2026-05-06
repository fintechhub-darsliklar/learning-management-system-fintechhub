from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.course.models import Course, Room


class CourseListSeralizer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseCreateSeralizer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class RoomListSeralizer(ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class RoomCreateSeralizer(ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"






