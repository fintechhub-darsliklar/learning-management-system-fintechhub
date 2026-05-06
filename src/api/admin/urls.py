from django.urls import path, include
from api.admin.views import students_views


urlpatterns = [
    path('student/', students_views.StudentListApiView.as_view()),
    path('student/create/', students_views.StudentCreateApiView.as_view()),
]
