from rest_framework.generics import ListAPIView, CreateAPIView
from api.admin.seralizers import group_seralizers
from apps.course.models import Group


class GroupListApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = group_seralizers.GroupListSeralizer


class GroupCreateApiView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = group_seralizers.GroupCreateSeralizer

