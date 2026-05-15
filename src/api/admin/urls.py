from django.urls import path, include
from api.admin.views import students_views
from api.admin.views import teacher_views
from api.admin.views import group_views
from api.admin.views import course_views
from api.admin.views import attandance_views


urlpatterns = [
    path('student/', students_views.StudentListApiView.as_view()),
    path('student/create/', students_views.StudentCreateApiView.as_view()),
    path('student/<int:pk>/', students_views.StudentRetrieveDestroyAPIView.as_view()),
    path('teacher/', teacher_views.TeacherListApiView.as_view()),
    path('teacher/create/', teacher_views.TeacherCreateApiView.as_view()),
    path('group/', group_views.GroupListApiView.as_view()),
    path('group/create/', group_views.GroupCreateApiView.as_view()),
    path('course/', course_views.CourseListApiView.as_view()),
    path('course/create/', course_views.CourseCreateApiView.as_view()),
    path('attandance/', attandance_views.StudentAttandanceListApiView.as_view()),
    path('attandance/create/', attandance_views.StudentAttandanceCreateApiView.as_view()),
]