from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import student_seralizers
from apps.student.models import Student



class StudentListApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = student_seralizers.StudentListSeralizer


class StudentCreateApiView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = student_seralizers.StudentCreateSeralizer

