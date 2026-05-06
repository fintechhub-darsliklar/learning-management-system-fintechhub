from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.student.models import StudentAttandance


class StudentAttandanceListSeralizer(ModelSerializer):

    class Meta:
        model = StudentAttandance
        fields = "__all__"


class StudentAttandanceCreateSeralizer(ModelSerializer):

    class Meta:
        model = StudentAttandance
        fields = "__all__"








