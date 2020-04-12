from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import mixins,GenericAPIView
from rest_framework import viewsets,views
from django.db.models import Q
from django.conf import settings
import random
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import BasePermission
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from users.models import User,VerifyCode
from student.models import Student
from student.serializers import StudentInfoSerializer,StudentBaseSerializer
from users.views import CustomBackend,jwt_response_payload_handler
from utils.common import retmessage,randm_photo
from utils.verifyclass import Verify_args
from utils.permissions import IsOwnerOrReadOnly



class StudentRegViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''学生注册'''
    serializer_class = StudentBaseSerializer
    queryset = User.objects.all()

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
        user = User.objects.create(mobile=mobile,username=mobile,password = make_password(password),is_student=True)
        student_obj = Student.objects.create(user=user,photo=randm_photo(),type="")

        payload = jwt_payload_handler(user)
        data =  {
            "id":user.id,
            "token": jwt_encode_handler(payload),
            "mobile":user.mobile,
            "user_name":user.name if user.name else user.username,
            "photo": str(student_obj.photo),
            "type": "student",
        }
        return Response(retmessage(0,"注册成功",data=data))



class StudentPwdViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''学生改密码'''
    serializer_class = StudentBaseSerializer
    queryset = User.objects.all()
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
        if Verify_args.changepwd_right_check(code,mobile,password):
            return Response(Verify_args.changepwd_right_check(code,mobile,password))
        #通过校验，修改学生信息
        user = User.objects.filter(mobile=mobile)[0]
        user.mobile = mobile
        user.password = make_password(password)
        user.username = mobile
        user.save()
        #返回值赋值
        photo = ""
        user_name = ""
        try:
            if user.students:
                photo = user.students.photo
                user_name = user.students.name
        except:
            pass
        payload = jwt_payload_handler(user)
        data =  {
            "id":user.id,
            "token": jwt_encode_handler(payload),
            "mobile":user.mobile,
            "user_name":user_name,
            "photo": str(photo),
            "type": "student",
        }
        return Response(retmessage(0,"修改密码成功",data=data))







class StudentInfoViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = StudentInfoSerializer

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
    def list(self, request, *args, **kwargs):
        '''查看个人信息'''
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            return Response(retmessage(1,"请填写个人信息"))
        payload = jwt_payload_handler(self.request.user)
        student_obj = Student.objects.filter(user=self.request.user)[0]
        data = {
            "id": student_obj.user.id,
            "token": jwt_encode_handler(payload),
            "mobile": student_obj.user.mobile,
            "user_name": student_obj.name,
            "photo": str(student_obj.photo),
            "type": "student",
        }

        return Response(retmessage(1,"查看个人信息",data=data))
    def create(self, request, *args, **kwargs):
        '''修改个人信息'''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data["name"]
        photo = ""
        if Verify_args.student_info_check(name,):
            return Response(Verify_args.student_info_check(name,))
        student_obj = Student.objects.filter(user=self.request.user)[0]
        student_obj.name = name
        student_obj.save()
        User.objects.filter(id=self.request.user.id).update(name=name)


        payload = jwt_payload_handler(self.request.user)
        data = {
            "id": student_obj.user.id,
            "token": jwt_encode_handler(payload),
            "mobile": student_obj.user.mobile,
            "user_name": student_obj.name,
            "photo": str(student_obj.photo),
            "type": "student"
        }

        return Response(retmessage(0,"修改个人信息成功",data=data))

