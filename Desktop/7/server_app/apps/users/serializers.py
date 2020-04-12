from rest_framework import serializers
import re
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator
from users.models import VerifyCode,User,UploadPhoto,StaticPhoto,StaticClassPhoto
from teacher.models import Teachers
from utils.common import retmessage

class SmsSerializer(serializers.Serializer):
    '''发送短信序列化器'''
    mobile = serializers.CharField(help_text="手机号",max_length=13,min_length=11)
    type = serializers.CharField(help_text="类型",required=True)

    # def validate_type(self, type):
    #     if not type:
    #         raise serializers.ValidationError("请选择类型")

    def validate_mobile(self, mobile):
        # print(self.initial_data['mobile'],"11111111111")
        verify_type = User.objects.filter(username=mobile)
        if not re.match(r'^(\+?64|0)2\d{7,9}$', mobile) and not re.match(
                r'^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$', mobile):
            raise serializers.ValidationError("手机号码非法")
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)

        # v_type = self.initial_data['type']

        if self.initial_data['type'] == "0":
            print(self.initial_data['type'],type(self.initial_data['type']))
            print(verify_type)
            if verify_type:
                print(">>>>>>>>>>>>>>>>>")
                raise serializers.ValidationError("该手机号已注册")
            # 验证码发送频率
            if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
                raise serializers.ValidationError("距离上一次发送未超过60s")
            return mobile
        elif self.initial_data['type'] == "1":
            if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
                raise serializers.ValidationError("距离上一次发送未超过60s")
            return mobile
        else:
            raise serializers.ValidationError("输入错误")


class SubmitPhotoSerializer(serializers.ModelSerializer):
    '''提交头像序列化'''
    photo_url = serializers.ImageField(required=True)
    class Meta:
        model = UploadPhoto
        fields = ("photo_url",)
        # extra_kwargs = {
        #     "photo_url":{'required': True}
        # }






