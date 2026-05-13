from django.urls import path, include
from api.admin.views import students_views, admin_views
\

urlpatterns = [
    path('student/', students_views.StudentListApiView.as_view()),
    path('student/create/', students_views.StudentCreateApiView.as_view()),
    path('admin/', admin_views.UserListApiView.as_view()),  
    path('admin/create/', admin_views.UserCreateApiView.as_view()),

]