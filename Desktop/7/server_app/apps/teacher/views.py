

from datetime import datetime
from datetime import timedelta
from django.contrib.auth import get_user_model
from rest_framework.generics import mixins,GenericAPIView
from rest_framework import viewsets,views
from rest_framework.views import APIView
from django.db.models import Q
from django.conf import settings
import random
import re
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import BasePermission
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FileUploadParser,JSONParser

from users.models import User,VerifyCode,StaticPhoto,UploadPhoto
from teacher.models import Teachers
from student.models import Student
from teacher.serializers import TeacherBaseSerializer,TeacherInfoSerializer,TeacherInfoSerializer1,PhotoSerializer

from users.views import CustomBackend,jwt_response_payload_handler
from utils.common import retmessage,randm_photo
from utils.verifyclass import Verify_args
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication









class TeacherRegViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''老师注册'''
    serializer_class = TeacherBaseSerializer
    queryset = User.objects.all()
    # parser_classes = (MultiPartParser, JSONParser)

    def create(self, request, *args, **kwargs):
        ret ={}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data["code"]
        mobile = serializer.validated_data["mobile"]
        password = serializer.validated_data["password"]
        #校验
        if Verify_args.none_check(code,mobile,password):
            return Response(Verify_args.none_check(code,mobile,password))
        if Verify_args.reg_right_check(code,mobile,password):
            return Response(Verify_args.reg_right_check(code,mobile,password))
        #通过校验，创建用户
        user = User.objects.create(mobile=mobile,username=mobile,password = make_password(password),is_teacher=True)
        #创建随机头像
        photo_obj = StaticPhoto.objects.all()
        # print(len(photo_obj))
        photo_list = []
        for i in photo_obj:
            photo_list.append(i.photo_url)

        randm_photo = photo_list[random.randint(0, len(photo_list) - 1)]
        print(randm_photo, "xxxxxxxxxxx")

        teacher_obj = Teachers.objects.create(photo=randm_photo,user_id=user.id)
        print(teacher_obj.photo)

        payload = jwt_payload_handler(user)
        data =  {
            "id":user.id,
            "token": jwt_encode_handler(payload),
            "mobile":user.mobile,
            "user_name":user.name if user.name else user.username,
            "photo": str(teacher_obj.photo),
            "type": teacher_obj.teacher_type,
        }
        return Response(retmessage(0,"注册成功",data=data))



class TeacherPwdViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''老师改密码'''
    serializer_class = TeacherBaseSerializer
    queryset = User.objects.all()
    def create(self, request, *args, **kwargs):
        ret ={}
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data["code"]
        mobile = serializer.validated_data["mobile"]
        password = serializer.validated_data["password"]
        #校验
        if Verify_args.none_check(code,mobile,password):
            return Response(Verify_args.none_check(code,mobile,password))
        if Verify_args.changepwd_right_check(code,mobile,password):
            return Response(Verify_args.changepwd_right_check(code,mobile,password))
        #通过校验，修改老师信息
        user = User.objects.filter(mobile=mobile)[0]
        user.mobile = mobile
        user.password = make_password(password)
        user.username = ""
        user.save()
        #返回值赋值
        photo = ""
        type = ""
        user_name = user.username
        try:
            if user.teachers:
                photo = user.teachers.photo
                type = user.teachers.teacher_type
                user_name = user.teachers.name
        except:
            pass
        payload = jwt_payload_handler(user)
        data =  {
            "id":user.id,
            "token": jwt_encode_handler(payload),
            "mobile":user.mobile,
            "user_name":user_name,
            "photo": str(photo),
            "type": type,
        }
        return Response(retmessage(0,"修改密码成功",data=data))







class TeacherInfoViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = TeacherInfoSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get_queryset(self):
        return Teachers.objects.filter(user=self.request.user)
    def get_serializer_class(self):
        if self.action == "list":
            return TeacherInfoSerializer
        return TeacherInfoSerializer1
    def list(self, request, *args, **kwargs):
        '''查看个人信息'''
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data[0]["photo"])


        # if not queryset:
        #     return Response(retmessage(1,"请填写个人信息"))
        payload = jwt_payload_handler(self.request.user)
        teacher_obj = Teachers.objects.filter(user=self.request.user)[0]
        data = {
            "id": teacher_obj.user.id,
            "token": jwt_encode_handler(payload),
            "mobile": teacher_obj.user.mobile,
            "user_name": teacher_obj.name,
            "photo": str(serializer.data[0]["photo"]),
            "type": teacher_obj.teacher_type,
        }

        return Response(retmessage(1,"查看个人信息",data=data))
    def create(self, request, *args, **kwargs):
        '''修改个人信息'''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]
        teacher_type = serializer.validated_data["teacher_type"]
        photo = serializer.validated_data["photo"]
        print(teacher_type)
        if Verify_args.teacher_info_check(name,teacher_type):
            return Response(Verify_args.teacher_info_check(name,teacher_type))
        Teachers.objects.update_or_create(user=self.request.user,defaults={"name":name,
                                                                           "teacher_type":teacher_type,})
        User.objects.filter(id=self.request.user.id).update(name=name)
        teacher_obj = Teachers.objects.filter(user=self.request.user)[0]
        teacher_obj.name = name
        teacher_obj.teacher_type = teacher_type
        teacher_obj.save()
        print(str(teacher_obj.photo))

        payload = jwt_payload_handler(self.request.user)
        data = {
            "id": teacher_obj.user.id,
            "token": jwt_encode_handler(payload),
            "mobile": teacher_obj.user.mobile,
            "user_name": teacher_obj.name,
            "photo": str(teacher_obj.photo),
            "type": teacher_obj.teacher_type,
        }

        return Response(retmessage(0,"修改个人信息成功",data=data))

# class SubmitPhotoViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
# class SubmitPhotoViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
#
#     permission_classes = (IsAuthenticated,)
#     serializer_class = SubmitPhotoSerializer
#     queryset = Teachers.objects.all()
#     # queryset = Teachers.objects.all()
#     parser_classes = (MultiPartParser,FileUploadParser)
#
#     # def get_serializer_class(self):
#     #     if self.request.user.is_teacher:
#     #         return SubmitPhotoSerializer
#     #     return SubmitPhotoSerializer1
#     def get_queryset(self):
#         if self.request.user.is_teacher:
#             # print(Teachers.objects.filter(user_id=2).values("photo"))
#             return Teachers.objects.filter(user_id=self.request.user.id)
#         return Student.objects.filter(user_id=self.request.user.id)
#     #
#     #
#     # def create(self, request, *args, **kwargs):
#     #     instance = self.get_object()
#     #     serializer = self.get_serializer(instance,data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     print(serializer.validated_data["photo"],"________________")
#     #     print(serializer,"11111111")
#     #     self.perform_create(serializer)
#     #     # headers = self.get_success_headers(serializer.data)
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def perform_create(self, serializer):
#     #     serializer.save()
#     #     print(serializer, "22222222222")
#
#
#     # def create(self, request, *args, **kwargs):
#     #     '''上传头像信息'''
#     #     print(self.request.user.is_teacher)
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     if self.request.user.is_teacher:
#     #         teacher_obj = Teachers.objects.filter(user=self.request.user)[0]
#     #         if serializer.validated_data["photo"]:
#     #             print(serializer.validated_data["photo"])
#     #             teacher_obj.photo = str(serializer.validated_data["photo"])
#     #             teacher_obj.save()
#     #         return Response(retmessage(0,"头像信息",data=str(teacher_obj.photo)))
#     #     student_obj = Student.objects.filter(user=self.request.user)[0]
#     #     if serializer.validated_data["photo"]:
#     #         student_obj.photo = str(serializer.validated_data["photo"])
#     #         student_obj.save()
#     #     return Response(retmessage(0, "头像信息", data=str(student_obj.photo)))
#     #
#     #
#     # # def get_queryset(self):
#     # #     if self.request.user.is_teacher:
#     # #         return Teachers.objects.filter(user=self.request.user)
#     # #     return Student.objects.filter(user=self.request.user)
#     #
#     #
#     # def create(self, request, *args, **kwargs):
#     #     '''上传头像信息'''
#     #     print(self.request.user.is_teacher)
#     #     serializer = self.get_serializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     if self.request.user.is_teacher:
#     #         teacher_obj = Teachers.objects.filter(user=self.request.user)[0]
#     #         if serializer.validated_data["photo"]:
#     #             teacher_obj.photo = serializer.validated_data["photo"]
#     #             teacher_obj.save()
#     #         return Response(retmessage(0,"头像信息",data=str(teacher_obj.photo)))
#     #     student_obj = Student.objects.filter(user=self.request.user)[0]
#     #     if serializer.validated_data["photo"]:
#     #         student_obj.photo = serializer.validated_data["photo"]
#     #         student_obj.save()
#     #     return Response(retmessage(0, "头像信息", data=str(student_obj.photo)))



class Test(mixins.ListModelMixin,viewsets.GenericViewSet):

    # permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, JSONParser)
    queryset = StaticPhoto.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        sun = StaticPhoto.objects.all()
        print(len(sun))
        sun_list = []
        for i in sun:
            sun_list.append(i.photo_url)

        randm_photo = sun_list[random.randint(0,len(sun_list)-1)]
        print(randm_photo,"xxxxxxxxxxx")
        teacher_obj = UploadPhoto.objects.create(photo_url=randm_photo)
        print(teacher_obj.photo_url,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data[0])
        return Response(serializer.data)


