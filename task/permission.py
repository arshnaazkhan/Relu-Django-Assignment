from rest_framework import  permissions

# Permission classes for Super-admin, Teacher and Student Groups created in Groups section of admin panel

class SuperAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Super-admin').exists()


class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Teacher').exists()


class StudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Student').exists()
