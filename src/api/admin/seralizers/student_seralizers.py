from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.student.models import Student, StudentBallTransaction, StudentMessages
from api.admin.seralizers.admin_seralizers import UserListSeralizer
from apps.users.models import User


class StudentListSeralizer(ModelSerializer):
    user = UserListSeralizer(read_only=True)
    salom = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"

    def get_salom(self, obj):
        return "salom dunyo"


class StudentCreateSeralizer(ModelSerializer):
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(max_length=50, write_only=True)
    last_name = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = Student
        fields =  "__all__"
        
    def validate(self, input_data):
        email = input_data.get("email")
        try:
            u = User.objects.get(email=email)
        except:
            u = None
        if u:
            raise ValidationError("Bu email allaqachon ishlatilgan.")
        return input_data


    def create(self, validated_data):
        email = validated_data.get("email")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(first_name)
        user.save()
        admin_user = self.context['request'].user
        student = Student.objects.create(
            user=user,
            created_by = admin_user
        )
        return student

    


class StudentBallTransactionListSeralizer(ModelSerializer):

    class Meta:
        model = StudentBallTransaction
        fields = "__all__"



class StudentBallTransactionCreateSeralizer(ModelSerializer):

    class Meta:
        model = StudentBallTransaction
        fields = "__all__"


class StudentMessagesListSeralizer(ModelSerializer):

    class Meta:
        model = StudentMessages
        fields = "__all__"


class StudentMessagesCreateSeralizer(ModelSerializer):

    class Meta:
        model = StudentMessages
        fields = "__all__"



