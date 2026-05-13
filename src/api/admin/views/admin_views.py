from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import UserListSeralizer, UserCreateSeralizer
from apps.users.models import User

class UserListApiView(ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = admin_seralizers.UserListSeralizer

class UserCreateApiView(CreateAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = admin_seralizers.UserCreateSeralizer    



