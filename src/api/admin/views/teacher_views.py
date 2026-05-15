from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import teacher_seralizers
from apps.teacher.models import Teacher



class TeacherListApiView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = teacher_seralizers.TeacherListSeralizer


class TeacherCreateApiView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = teacher_seralizers.TeacherCreateSeralizer

