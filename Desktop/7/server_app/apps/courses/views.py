# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
#
# from courses import models
# from rest_framework.generics import mixins,GenericAPIView
# # Create your views here.
# from rest_framework.authentication import TokenAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
#
# from rest_framework.mixins import CreateModelMixin
# from rest_framework import mixins
# from rest_framework import viewsets
# from rest_framework import filters
# from rest_framework import status
#
# from courses.serializers import CoursesSerializers,CourseTimesSerializers,CourseTimesSerializers2,TaskSerializers
#
#
# class CourseViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
#     """
#     list:
#         课程数据
#     create:
#         新增课程
#     update:
#         更新课程
#     destroy:
#         删除课程
#     """
#     serializer_class = CoursesSerializers
#     queryset = models.CourseManagement.objects.all()
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         ret = {}
#         serializer = self.get_serializer(data=request.data)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         ret["status"] = status.HTTP_201_CREATED
#         ret["message"] = "创建课程成功"
#         ret["data"] = []
#         return Response(ret,headers=headers)
#         # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#     # def destroy(self, request, *args, **kwargs):
#     #     ret = {}
#     #     instance = self.get_object()
#     #     self.perform_destroy(instance)
#     #     ret["status"] = status.HTTP_204_NO_CONTENT
#     #     ret["message"] = "删除课程成功"
#     #     ret["data"] = []
#     #     return Response(ret)
#
#
# class CourseTimesViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
#     """
#         list:
#             课次数据
#         create:
#             新增课次
#         update:
#             更新课次
#         destroy:
#             删除课次
#         """
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CourseTimesSerializers
#     queryset = models.CourseTimes.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == "create":
#             return CourseTimesSerializers
#         return CourseTimesSerializers2
#
# class TaskViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = TaskSerializers
#     queryset = models.TaskList.objects.all()
#     lookup_field ="course_times_id"
#
#     '''
#     很重要的测试，跨表
#     def perform_create(self, serializer):
#         print(serializer,"asdasda")
#         task = serializer.save()
#         course_times =task.course_times
#         print(task)
#         obj = models.CourseTimes.objects.filter(course_times_name=course_times)[0]
#         print(obj)
#         obj.course_times_name = "xxxxxxxxxxx"
#         print(obj.course_times_name)
#         obj.save()
#         # for item in task:
#         #     print(item)
#     '''
#
#
#
#     # def create(self, request, *args, **kwargs):
#     #     print(request.data)
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     self.perform_create(serializer)
#     #     headers = self.get_success_headers(serializer.data)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
