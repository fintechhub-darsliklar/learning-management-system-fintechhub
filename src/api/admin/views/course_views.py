from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import course_seralizers
from apps.course.models import Course



class CourseListApiView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = course_seralizers.CourseListSeralizer


class CourseCreateApiView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = course_seralizers.CourseCreateSeralizer

