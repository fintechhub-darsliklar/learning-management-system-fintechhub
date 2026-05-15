from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from api.admin.seralizers import student_seralizers
from apps.student.models import Student
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from api.admin.permissions import CanThisActionPermission


class StudentListApiView(ListAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = student_seralizers.StudentListSeralizer
    permission_classes = [IsAuthenticated, CanThisActionPermission]


class StudentCreateApiView(CreateAPIView):
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser, CanThisActionPermission]
    serializer_class = student_seralizers.StudentCreateSeralizer
    

class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    permission_classes = [IsAuthenticated, IsAdminUser, CanThisActionPermission]

    def delete(self, request, pk):
        student = self.get_object()
        student.is_deleted = True
        student.deleted_by = request.user
        student.save()
        return Response({
            "message": "Student deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

