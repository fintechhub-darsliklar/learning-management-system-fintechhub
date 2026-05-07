from django.urls import path, include
from api.auth.views.login_view import LoginView


urlpatterns = [
    path('login/', LoginView.as_view()),
    # path('', include('api.admin.urls')),
    # path('', include('api.admin.urls')),
]
