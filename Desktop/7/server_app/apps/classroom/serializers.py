from rest_framework import serializers
from classroom.models import ClassRoom,ClassMember,ClassGroup,Card
from teacher.models import Teachers
import time


from rest_framework.validators import UniqueValidator


class ClassRoomSerializer(serializers.ModelSerializer):
    '''创建教室序列化器'''
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    print(user)
    room_num = serializers.CharField(read_only=True)
    room_name = serializers.CharField(label="教室名称", help_text="教室名称",default="")
    creater = serializers.CharField(read_only=True)
    creater_ch = serializers.CharField(read_only=True)
    def generate_room_num(self):
        '''自动生成房间号'''
        from random import Random
        random_ins = Random()
        room_num = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return room_num
    def validate(self, attrs):
        attrs["room_num"] = self.generate_room_num()
        return attrs

    class Meta:
        model = ClassRoom
        fields = ['id',"user","room_name","room_num","creater","creater_ch","school","grade"]


# class TeacherSerializer(serializers.ModelSerializer):
#     '''老师序列化器'''
#     # xxx = serializers.CharField(source="teacher_type")
#     # t_type = serializers.CharField(source="get_teacher_type_display")
#     # creater = serializers.SerializerMethodField() #自定义显示
#     # def get_creater(self,row):
#     class Meta:
#         model = Teachers
#         fields = ["name"]

class ClassSeacherSerializer(serializers.ModelSerializer):
    '''班级号搜索'''
    class Meta:
        model = ClassRoom
        fields = ['id',"creater","room_name","room_num","school","grade"]

class ClassInfoSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(), help_text="id",
    # )
    teacher_num = serializers.SerializerMethodField()
    student_num = serializers.SerializerMethodField()


    def get_teacher_num(self,obj):
        teachers= ClassMember.objects.filter(class_id =obj.id,member_type="teacher",status="inclass")
        teacher_num=len(teachers)
        return teacher_num
    def get_student_num(self,obj):
        student = ClassMember.objects.filter(class_id=obj.id, member_type="student",status="inclass")
        student_num = len(student)
        return student_num
    # student = ClassMember.objects
    class Meta:
        model = ClassRoom
        fields = ['id',"user","user_name","user_type","room_name","room_num","school","grade","student_num","teacher_num"]
        # depth = 1

class RemoveMemberSerializer(serializers.ModelSerializer):
    '''移出成员，退出教室序列化器'''
    class Meta:
        model = ClassMember
        fields = ['id',]
        # depth = 1

class ApplicationSerializer1(serializers.ModelSerializer):

    '''申请进入班级序列化器'''
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # room_num = serializers.CharField(max_length=64,help_text="教室号")
    # class_creater = serializers.CharField(max_length=64,help_text="班级创建者姓名")
    # class_creater_id = serializers.CharField(max_length=64,help_text="班级创建者id")
    # application_type = serializers.CharField(max_length=64,help_text=u"申请方式： link（链接邀请),seacher（搜索)")
    # Inviter = serializers.CharField(max_length=64,help_text="邀请人id")
    # room_name = serializers.SerializerMethodField(read_only=True)
    # def get_room_name(self,obj):
    #     print(obj.class_id_id,"++++++++++++++++")
    #     room_obj = ClassRoom.objects.filter(id =obj.class_id_id)[0]
    #     room_name=room_obj.room_name
    #     return room_name
    # application_result = serializers.CharField(source="get_application_result_display",help_text=u"(1, 通过),(2, 拒绝),(3, 待审核),")
    class_id = serializers.CharField(required=True)
    class Meta:
        model = ClassMember
        fields = ["id","user","class_id","application_type","Inviter"]


class ApplicationSerializer(serializers.ModelSerializer):
    '''审核列化器'''
    # room_num = serializers.CharField(max_length=64,help_text="教室号")
    # class_creater = serializers.CharField(max_length=64,help_text="班级创建者姓名")
    # class_creater_id = serializers.CharField(max_length=64,help_text="班级创建者id")
    # application_type = serializers.CharField(max_length=64,help_text=u"申请方式： link（链接邀请),seacher（搜索)")
    # Inviter = serializers.CharField(max_length=64,help_text="邀请人id")
    # room_name = serializers.SerializerMethodField(read_only=True)
    # def get_room_name(self,obj):
    #     print(obj.class_id_id,"++++++++++++++++")
    #     room_obj = ClassRoom.objects.filter(id =obj.class_id_id)[0]
    #     room_name=room_obj.room_name
    #     return room_name
    application_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    # application_result = serializers.CharField(source="get_application_result_display",help_text=u"(1, 通过),(2, 拒绝),(3, 待审核),")
    id = serializers.CharField(required=False)
    class Meta:
        model = ClassMember
        fields = ["id","class_id","user","user_name","user_type","school","mobile","application_type","application_time","Inviter_name","status","application_result"]
        read_only_fields = ('class_id',"user","user_name","user_type","school","mobile","application_type","application_time","Inviter_name","status")
        # fields = ['id',"room_name","class_id","user","application_type","Inviter"]
        #
        # depth = 1

class GroupSerializer(serializers.ModelSerializer):
    '''审核列化器'''
    # room_num = serializers.CharField(max_length=64,help_text="教室号")
    # class_creater = serializers.CharField(max_length=64,help_text="班级创建者姓名")
    # class_creater_id = serializers.CharField(max_length=64,help_text="班级创建者id")
    # application_type = serializers.CharField(max_length=64,help_text=u"申请方式： link（链接邀请),seacher（搜索)")
    # Inviter = serializers.CharField(max_length=64,help_text="邀请人id")
    # room_name = serializers.SerializerMethodField(read_only=True)
    # def get_room_name(self,obj):
    #     print(obj.class_id_id,"++++++++++++++++")
    #     room_obj = ClassRoom.objects.filter(id =obj.class_id_id)[0]
    #     room_name=room_obj.room_name
    #     return room_name

    class Meta:
        model = ClassMember
        fields = ["id","group"]


class FenZuSerializer(serializers.ModelSerializer):
    # application_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    # application_result = serializers.CharField(source="get_application_result_display",help_text=u"(1, 通过),(2, 拒绝),(3, 待审核),")
    id = serializers.CharField(required=True)
    group = serializers.CharField(required=True)
    photo = serializers.CharField(default="")
    class Meta:
        model = ClassMember
        fields = ["id", "class_id", "user", "user_name","call", "user_type","is_creater","group","group_num","photo"]
        read_only_fields = (
        'class_id', "user", "user_name", "call","is_creater", "user_type","group_num","photo")



class CardSerializer(serializers.ModelSerializer):
    '''卡片序列化器'''
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    img_url = serializers.SerializerMethodField(help_text="图片地址")
    def get_img_url(self,obj):
        img_obj = obj.clscard1.all()
        ret = []
        for item in role_obj_list:
            ret.append({"photo_url": item.photo_url})
        return ret
    class Meta:
        model = Card
        fields = ["id", "class_id", "comment", "reply_type","send_type", "add_time","status","is_send","img_url"]
