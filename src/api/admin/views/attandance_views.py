from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import attandance_seralizers
from apps.student.models import StudentAttandance



class StudentAttandanceListApiView(ListAPIView):
    queryset = StudentAttandance.objects.all()
    serializer_class = attandance_seralizers.StudentAttandanceListSeralizer


class StudentAttandanceCreateApiView(CreateAPIView):
    queryset = StudentAttandance.objects.all()
    serializer_class = attandance_seralizers.StudentAttandanceCreateSeralizer

