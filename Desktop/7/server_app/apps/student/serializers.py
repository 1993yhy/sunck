from rest_framework import serializers
import re
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from users.models import VerifyCode,User
from student.models import Student
from django.db.models import Q

class StudentBaseSerializer(serializers.ModelSerializer):
    '''学生注册和改密码的序列化器'''
    code = serializers.CharField(help_text="验证码", default="")
    mobile = serializers.CharField(help_text="电话号码", default="")
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True, default=""
    )

    class Meta:
        model = User
        fields = ("code", "mobile", "password")


class StudentInfoSerializer(serializers.ModelSerializer):
    '''学生填写个人信息'''
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), help_text="老师id",
    )

    name = serializers.CharField(label="姓名", help_text="姓名", default="")
    photo = serializers.CharField(label="头像", help_text="头像", read_only=True)

    class Meta:
        model = Student
        fields = ("user", "name", "photo")
