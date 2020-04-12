import re
from utils.common import retmessage
from users.models import VerifyCode,User
from classroom.models import ClassRoom
from teacher.models import Teachers
from datetime import datetime,timedelta

class Verify_args:
    @staticmethod
    def none_check(code=None,mobile=None,password=None):
        '''校验是否为空'''
        if not code:
            return retmessage(1,"验证码不能为空")
        if not mobile:
            return retmessage(1,"手机号不能为空")
        if not password:
            return retmessage(1,"密码不能为空")
    @staticmethod
    def reg_right_check(code=None,mobile=None,password=None):
        if not re.match(r'^(\+?64|0)2\d{7,9}$', mobile) and not re.match(
                r'^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$', mobile):
            return retmessage(1, "手机号码不合法")
        if len(password)>16 or len(password)<6:
            return retmessage(1,"密码必须保持在6-16位字符长度之间！")
        try:
            user_mobile = User.objects.filter(mobile=mobile)
            if user_mobile:
                return retmessage(1, "该手机号已注册")
        except:
            pass
        try:
            verify_records = VerifyCode.objects.filter(mobile=mobile).order_by("-add_time")
            '''校验验证码'''
            if verify_records:
                last_record = verify_records[0]
                five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
                if five_mintes_ago > last_record.add_time:
                    return retmessage(1,"验证码过期")
                if last_record.code != code:
                    return retmessage(1,"验证码错误")
                return None
            else:
                return retmessage(1,"验证码错误")
        except:
            return retmessage(1,"手机号输入有误")

    @staticmethod
    def changepwd_right_check(code=None, mobile=None, password=None):
        if not re.match(r'^(\+?64|0)2\d{7,9}$', mobile) and not re.match(
                r'^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$', mobile):
            return retmessage(1, "手机号码不合法")
        if len(password) > 16 or len(password) < 6:
            return retmessage(1, "密码必须保持在6-16位字符长度之间！")
        # user_mobile = User.objects.filter(mobile=mobile)
        if not User.objects.filter(mobile=mobile):
            return retmessage(1, "该手机号未注册")
        try:
            verify_records = VerifyCode.objects.filter(mobile=mobile).order_by("-add_time")
            '''校验验证码'''
            if verify_records:
                last_record = verify_records[0]
                five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
                if five_mintes_ago > last_record.add_time:
                    return retmessage(1, "验证码过期")
                if last_record.code != code:
                    return retmessage(1, "验证码错误")
                return None
            else:
                return retmessage(1,"验证码错误")
        except:
            return retmessage(1,"手机号输入有误")

    @staticmethod
    def teacher_info_check(name=None, teacher_type=None):
        '''校验用户填写个人信息是否合法'''
        if not name:
            return retmessage(1, "姓名不能为空")
        if not teacher_type:
            return retmessage(1, "请选择老师类型")

    @staticmethod
    def student_info_check(name=None):
        '''校验用户填写个人信息是否合法'''
        if not name:
            return retmessage(1, "姓名不能为空")

    @staticmethod
    def class_create_check(room_name=None, grade=None):
        '''校验创建班级参数'''
        if not room_name:
            return retmessage(1, "班级名不能为空")
        if not grade:
            return retmessage(1, "请选择年级")
        if ClassRoom.objects.filter(room_name=room_name):
            return retmessage(1,"教室名重复")





