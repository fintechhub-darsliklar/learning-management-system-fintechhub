from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.teacher.models import Teacher, Specialty


class TeacherListSeralizer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"



class SpecialtyListSeralizer(ModelSerializer):

    class Meta:
        model = Specialty
        fields = "__all__"



class TeacherCreateSeralizer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"



class SpecialtyCreateSeralizer(ModelSerializer):

    class Meta:
        model = Specialty
        fields = "__all__"




