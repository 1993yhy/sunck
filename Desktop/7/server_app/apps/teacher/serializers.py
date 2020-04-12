from rest_framework import serializers
import re
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from users.models import VerifyCode,User
from teacher.models import Teachers
from student.models import Student
from users.models import StaticPhoto,StaticClassPhoto
from django.db.models import Q

class TeacherBaseSerializer(serializers.ModelSerializer):
    '''老师注册和改密码的序列化器'''
    code = serializers.CharField(help_text="验证码",default="")
    mobile = serializers.CharField(help_text="电话号码",default="")
    # mobile = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
    #                                  validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,default=""
    )

    class Meta:
        model = User
        fields = ("code", "mobile", "password")



class TeacherInfoSerializer(serializers.ModelSerializer):
    '''老师填写个人信息'''
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),help_text="老师id",
    )

    name = serializers.CharField(label="姓名", help_text="姓名",default="")
    # photo = serializers.CharField(label="头像", help_text="头像")
    photo = serializers.ImageField(label="头像", help_text="头像")

    class Meta:
        model = Teachers
        fields = ( "user", "name","teacher_type","photo")

class TeacherInfoSerializer1(serializers.ModelSerializer):
    '''老师填写个人信息'''
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),help_text="老师id",
    )

    name = serializers.CharField(label="姓名", help_text="姓名",default="")
    # photo = serializers.CharField(label="头像", help_text="头像")
    photo = serializers.CharField(label="头像", help_text="头像")

    class Meta:
        model = Teachers
        fields = ( "user", "name","teacher_type","photo")


# class SubmitPhotoSerializer(serializers.ModelSerializer):
#     '''老师提交头像序列化'''
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault(),help_text="老师id",
#     )
#     # photo = serializers.ImageField(label="头像", help_text="头像")
#
#     class Meta:
#         model = Teachers
#         fields = ( "user", "photo")

# class SubmitPhotoSerializer1(serializers.ModelSerializer):
#     '''学生提交头像序列化'''
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault(),help_text="老师id",
#     )
#     # photo = serializers.ImageField(label="头像", help_text="头像")
#
#     class Meta:
#         model = Student
#         fields = ( "user", "photo")


class PhotoSerializer(serializers.ModelSerializer):
    '''提交头像序列化'''
    photo_url = serializers.ImageField(required=True)
    class Meta:
        model = StaticPhoto
        fields = ("photo_url",)