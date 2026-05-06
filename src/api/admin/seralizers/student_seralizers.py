from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from apps.student.models import Student, StudentBallTransaction, StudentMessages


class StudentListSeralizer(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentCreateSeralizer(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


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



