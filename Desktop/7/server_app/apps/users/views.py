from rest_framework.generics import mixins,GenericAPIView
from rest_framework import viewsets,views
from django.db.models import Q
import random
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework.parsers import JSONParser
import requests
import re
from rest_framework.parsers import MultiPartParser,FileUploadParser

from users.models import User,VerifyCode,UploadPhoto,StaticPhoto,StaticClassPhoto
from users.serializers import SmsSerializer,SubmitPhotoSerializer
from django.contrib.auth.backends import ModelBackend
from utils.common import retmessage
# User = get_user_model()
#
def getUserName(user):
    if user.is_teacher:
        return user.teachers.name
    elif user.is_student:
        return user.students.name
    return user.name

def jwt_response_payload_error_handler(serializer, request = None):
    return {
        "msg": "用户名或者密码错误",
        "code": 1,
        "detail": serializer.errors
    }

def jwt_response_payload_handler(token, user=None, request=None):


    data = {
        "id":user.id,
        "token": token,
        "mobile": user.mobile,
        "user_name":"",
        "photo": "",
        "type": "",
    }

    try:
        if user.students:
            data["user_name"] = user.students.name
            data["type"] = user.students.type
            data["photo"] = str(user.students.photo)
    except:
        try:
            if user.teachers:
                data["user_name"] = user.teachers.name
                data["photo"] = str(user.teachers.photo)
                data["type"] = user.teachers.teacher_type

        except:
            data["user_name"] = user.username

    ret=retmessage(0,"登陆成功",data)

    return ret
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self,request,username=None, password=None,**kwargs):
        try:
            user = User.objects.filter(Q(username=username)|Q(mobile=username)).first()
            if user is None :
                raise serializers.ValidationError(retmessage(1,"您的账户输入有误",))
            elif user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                raise serializers.ValidationError(retmessage(1, "密码有误",))
        except User.DoesNotExist :
            raise serializers.ValidationError(retmessage(0, "你账户输入有误",))






class SmsCodeViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''发送短信验证码'''
    serializer_class = SmsSerializer
    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '0123456789'
        return ''.join(random.sample(seeds, 6))

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        # type = serializer.validated_data["type"]


        str = "[AI Yi Education]Your phone verification code is:"
        code = self.generate_code()
        sms = requests.get(
            "http://api.smsglobal.com/http-api.php?action=sendsms&user=ayiu11ia&password=dPoSXQB6&from=Test&to=%s&text=%s%s" % (
                mobile, str, code))
        print('sms',sms)
        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        data = {"sms": code}
        return Response(retmessage(0, "短信发送成功", data),status=status.HTTP_200_OK)

class SubmitPhotoViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = SubmitPhotoSerializer
    queryset = UploadPhoto.objects.all()
    # queryset = Teachers.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser)

    def list(self, request, *args, **kwargs):
        base1 = request.META.get('HTTP_HOST')
        base2 = "http://"+base1 + "/media"
        print(base2)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # print(serializer.data[0]['photo_url'])
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        print(serializer.validated_data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()








