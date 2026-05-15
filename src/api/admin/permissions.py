from rest_framework import permissions


class CanThisActionPermission(permissions.BasePermission):

    def has_permission(self, request, *args, **kwargs):
        # if request.user.email == 'test@mail.com':
        #     return True
        print(request.user.is_superuser)
        perm = request.user.has_perm('student.view_student')
        print(perm)
        print(kwargs)
        return perm