from rest_framework import permissions
from classroom.models import ClassMember

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class MyPermission1(permissions.BasePermission):
    '''老师才能访问的权限'''
    def has_permission(self,request,view):
        if request.user.is_teacher ==True:
            return True
        return False

class MyPermission2(permissions.BasePermission):
    '''只有创建者才能访问的权限'''
    def has_permission(self,request,view):
        teacher_id = request.user.id
        if ClassMember.objects.filter(examine_man_id=teacher_id):
            return True
        return False
        # if request.user.is_teacher ==True:
