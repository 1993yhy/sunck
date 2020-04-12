from django.db import models
from users.models import User
from datetime import datetime



class ClassRoom(models.Model):
    '''教室信息'''
    grade_type = (
        (1, "一年级"),
        (2, "二年级"),
        (3, "三年级"),
        (4, "四年级"),
        (5, "五年级"),
        (6, "六年级"),
        (7, "七年级"),
        (8, "八年级"),
        (9, "九年级"),
        (10, "十年级"),
        (11, "十一年级"),
        (12, "十二年级"),
    )

    user = models.ForeignKey(User,null=True, blank=True, verbose_name="创建人", help_text="创建人",
                                        related_name="teacher", on_delete=models.CASCADE)
    room_num = models.CharField(max_length=64, null=True, blank=True, unique=True, verbose_name="教室号",help_text="教室号")
    room_name = models.CharField(default="",max_length=128,  verbose_name="教室名称",help_text="教室名称")
    school = models.CharField(null=True,blank=True,max_length=128,  verbose_name="学校",help_text="学校")
    grade = models.IntegerField(choices=grade_type, default=3, verbose_name="年级",help_text="年级")

    class Meta:
        db_table = "classroom"
        verbose_name = "教室信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.room_name

    @property
    def creater(self):
        """创建者名字"""
        return self.user.teachers.name

    @property
    def creater_ch(self):
        """创建者称呼"""
        return self.user.teachers.teacher_type
    @property
    def user_name(self):
        """用户姓名"""
        return self.user.name

    @property
    def user_type(self):
        """用户姓名"""
        if self.user.is_student:
            return "student"
        else:
            return "teacher"
    # @property
    # def is_creater(self):
    #     print(self.classmember.examine_man)
    #     if self.classmember.examine_man:
    #         return True
    #     else:
    #         return False
        #     return True
        # else:
        #     return False
    # @property
    # def teacher_num(self):
    #     num = len(self.clsroom.filter(member_type="teacher"))
    #     return num
    # @property
    # def student_num(self):
    #     num = len(self.clsroom.filter(member_type="student"))
    #     return num

class ClassMember(models.Model):
    '''教室成员'''
    membertype = (
        ("teacher", "老师"),
        ("student", "学生"),
    )
    apptype = (
        ("link", "链接邀请"),
        ("seacher", "搜索"),
        ("creater","创建者")
    )
    result = (
        (1, "通过"),
        (2, "拒绝"),
        (3, "待审核"),
    )
    status = (
        ("inclass", "在教室"),
        ("outclass", "不在教室"),
    )
    groups = (
        (0, "未分组"),
        (1, "一组"),
        (2, "二组"),
        (3, "三组"),
        (4, "四组"),
        (5, "五组"),
        (6, "六组"),
        (7, "七组"),
        (8, "八组"),
        (9, "九组"),
        (10, "十组"),
    )

    class_id = models.ForeignKey(ClassRoom, null=True, blank=True, verbose_name="教室id", help_text="教室id",
                                        related_name="clsroom", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, verbose_name="人员信息", help_text="人员信息",
                                        related_name="class_user", on_delete=models.CASCADE)
    member_type = models.CharField(choices=membertype, default="", max_length=30, verbose_name="成员类型", help_text="成员类型")
    application_time = models.DateTimeField(default=datetime.now, verbose_name="申请时间", help_text="申请时间")
    application_type = models.CharField(choices=apptype, default="", max_length=30, verbose_name="申请方式", help_text="申请方式")
    application_result = models.IntegerField(choices=result, blank=True,null=True,default=3, verbose_name="申请结果",help_text="申请结果")
    Inviter = models.ForeignKey(User, null=True, blank=True, verbose_name="邀请人", help_text="邀请人",
                                        related_name="inviter_user", on_delete=models.CASCADE)
    status = models.CharField(choices=status, default="", max_length=30, verbose_name="状态", help_text="状态")
    group = models.IntegerField(choices=groups, default=0, verbose_name="分组",help_text="分组")
    examine_man = models.ForeignKey(User, null=True, blank=True, verbose_name="审核人员", help_text="审核人员",
                                    related_name="tea1", on_delete=models.CASCADE)
    examine_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="审核时间")

    class Meta:
        db_table = "classmember"
        verbose_name = "教室成员信息"
        verbose_name_plural = verbose_name
    @property
    def user_name(self):
        """用户姓名"""
        return self.user.name
    @property
    def user_type(self):
        """用户类型"""
        # try:
        #     if self.user.is_teacher:
                # print(self.user.teachers.t_type)
                # print(self.user.teachers.teacher_type)
                # tp = ""
                # for i in self.user.teachers.t_type:
                #     if i=="Dr":
                #         tp = 0
                #     elif i=="Mr":
                #         tp = 1
                #     elif i=="Miss":
                #         tp = 2
                #     else:
                #         tp = 3
                # return self.user.teachers.t_type[tp][0]
                # return self.t_type[self.teacher_type][1] + ":" + self.name
        # except:
        #     return "student"
        if self.user.is_teacher:
            return "teacher"
        elif self.user.is_student:
            return "student"

    @property
    def school(self):
        return self.class_id.school

    @property
    def mobile(self):
        return self.user.mobile

    @property
    def Inviter_name(self):
        return self.Inviter.name

    @property
    def call(self):
        try:
            if self.user.teachers:
                return self.user.teachers.teacher_type
            else:
                return ""
        except:
            return ""
    @property
    def is_creater(self):
        if self.examine_man:
            return True
        else:
            return False

    @property
    def group_num(self):
        obj = ClassMember.objects.filter(class_id_id=self.class_id_id,group=self.group,status="inclass")
        return len(obj)




    # def __str__(self):
    #     return self.class_id


class ClassGroup(models.Model):
    '''分组表'''
    results = (
        (1, "通过"),
        (2, "拒绝"),
    )
    groups = (
        (0, "未分组"),
        (1, "一组"),
        (2, "二组"),
        (3, "三组"),
        (4, "四组"),
        (5, "五组"),
        (6, "六组"),
        (7, "七组"),
        (8, "八组"),
        (9, "九组"),
        (10, "老师组"),
    )
    class_id = models.ForeignKey(ClassRoom, null=True, blank=True, verbose_name="教室id", help_text="教室id",
                                       related_name="room", on_delete=models.CASCADE)
    members = models.ForeignKey(ClassMember, null=True, blank=True, verbose_name="成员", help_text="成员",
                                 related_name="classmember", on_delete=models.CASCADE)
    group = models.IntegerField(choices=groups, default=0, verbose_name="分组",help_text="分组")
    group_num = models.IntegerField( default=0,verbose_name="分组人数",help_text="分组人数")


    class Meta:
        db_table = "classgroup"
        verbose_name = "分组表"
        verbose_name_plural = verbose_name

#老师卡片显示
# class Showkapian(models.Model):
#     '''可保存到草稿'''
#     id =
#     卡片名 =
#     卡片描述 = 文字
#     附件 =  照片，视频（用于描述卡片）
#     描述类型 = 照片，视频，文字
#     添加知识点 = 待定
#     答复类型 = NO，text，video,phot,自定义
#     答复内容 = (自定义，左老师提的问题，右学生回答)
#     是否是发给全部学生 =
#     选择发送组 = (优先展示组，接下来是个人)
#     选择发送个人 =
#     是否是草稿 =

#上传图片接口，同步到oss
#uml数据库

class Card(models.Model):
    '''卡片信息'''
    r_type = (
        (0, "no"),
        (1, "text"),
        (2, "video"),
        (3, "photo"),
        (4, "customize"),
    )
    r_status = (
        (0, "noreply"),
        (1, "replyed"),
    )
    s_type= (
        (0, "allpeople"),
        (1, "somepeople"),
        (2, "allgroup"),
        (3, "somegroup"),
    )
    i_send = (
        (0, "send"),
        (1, "save"),
    )

    class_id = models.ForeignKey(ClassRoom,null=True, blank=True, verbose_name="关联教室", help_text="关联教室",
                                        related_name="clscard", on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=True, blank=True, unique=True, verbose_name="卡片标题",help_text="卡片标题")
    comment = models.CharField(default="",max_length=254,  verbose_name="卡片内容",help_text="卡片内容")
    reply_type = models.IntegerField(choices=r_type,default=0,verbose_name="回复类型",help_text=u"回复类型: 0(no),1(text),2(video),3(photo),4(customize)")
    send_type = models.IntegerField(choices=s_type,default=0,verbose_name="发送类型",help_text=u"发送类型: 0(allpeople),1(somepeople),2(allgroup),3(somegroup)")
    add_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="创建时间")
    status = models.IntegerField(choices=r_status,default=0,verbose_name="回复状态",help_text=u"回复状态: 0(noreply),1(replyed)")
    is_send = models.IntegerField(choices=i_send,default=0,verbose_name="发送状态",help_text=u"发送状态: 0(发送),1(保存)")
    class Meta:
        db_table = "classcard"
        verbose_name = "卡片信息"
        verbose_name_plural = verbose_name


class Photo(models.Model):
    '''图片信息'''
    imgs = models.ForeignKey(Card, null=True, blank=True, verbose_name="图片集", help_text="图片集",
                             related_name="clscard1", on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, blank=True, verbose_name="创建人", help_text="创建人",
                                        related_name="clsuser1", on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="图片地址",help_text="图片地址")

    add_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="创建时间")
    class Meta:
        db_table = "classphoto"
        verbose_name = "图片信息"
        verbose_name_plural = verbose_name

class Video(models.Model):
    '''视频信息'''
    video = models.ForeignKey(Card, null=True, blank=True, verbose_name="视频集", help_text="视频集",
                             related_name="clscard2", on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, blank=True, verbose_name="创建人", help_text="创建人",
                                        related_name="clsuser2", on_delete=models.CASCADE)
    video_url = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="视频地址",help_text="视频地址")

    add_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="创建时间")
    class Meta:
        db_table = "classvideo"
        verbose_name = "视频信息"
        verbose_name_plural = verbose_name

class ChoiceQuestion(models.Model):
    '''选择题信息'''
    question = models.ForeignKey(Card, null=True, blank=True, verbose_name="视频集", help_text="视频集",
                             related_name="clscard3", on_delete=models.CASCADE)
    question_comment = models.CharField(default="", max_length=254, verbose_name="选择题内容", help_text="选择题内容")
    user = models.ForeignKey(User,null=True, blank=True, verbose_name="创建人", help_text="创建人",
                                        related_name="clsuser3", on_delete=models.CASCADE)
    option1 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项1",help_text="选项1")
    option2 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项2", help_text="选项2")
    option3 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项3", help_text="选项3")
    option4 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项4", help_text="选项4")
    option5 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项5", help_text="选项5")
    option6 = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项6", help_text="选项6")
    answer = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="答案", help_text="答案")

    add_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="创建时间")
    class Meta:
        db_table = "classchoicequestion"
        verbose_name = "选择题信息"
        verbose_name_plural = verbose_name


class StudentReply(models.Model):
    '''学生回复信息'''
    r_status = (
        (0, "noreply"),
        (1, "replyed"),
    )
    card_id = models.ForeignKey(Card, null=True, blank=True, verbose_name="关联卡片", help_text="关联卡片",
                             related_name="clscard4", on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, blank=True, verbose_name="答题人", help_text="答题人",
                                        related_name="clsuser4", on_delete=models.CASCADE)
    text = models.CharField(max_length=254, null=True, blank=True, unique=True, verbose_name="回复内容",help_text="回复内容")
    img_url = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="图片地址", help_text="图片地址")
    video_url = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="视频地址", help_text="视频地址")
    question_answer = models.CharField(max_length=128, null=True, blank=True, unique=True, verbose_name="选项题答案", help_text="选项题答案")
    reply_status = models.IntegerField(choices=r_status,default=0,verbose_name="回复状态",help_text="回复状态")
    reply_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="回复时间", help_text="回复时间")

    class Meta:
        db_table = "studentreply"
        verbose_name = "学生回复"
        verbose_name_plural = verbose_name



class TeacherLable(models.Model):
    '''老师标签'''
    teacher_lable = models.ForeignKey(StudentReply, null=True, blank=True, verbose_name="老师标签", help_text="老师标签",
                             related_name="tealab", on_delete=models.CASCADE)

    class Meta:
        db_table = "teacherlable"
        verbose_name = "老师标签"
        verbose_name_plural = verbose_name

class CommentFrom(models.Model):
    '''评论表'''
    student_reply = models.ForeignKey(StudentReply, null=True, blank=True, verbose_name="老师标签", help_text="老师标签",
                             related_name="teacom", on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, blank=True, verbose_name="创建人", help_text="创建人",
                                        related_name="clsuser5", on_delete=models.CASCADE)
    comment = models.CharField(max_length=254, null=True, blank=True, unique=True, verbose_name="评论内容",help_text="评论内容")
    parent_id = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目", help_text="父目录",
                                        related_name="teaparent", on_delete=models.CASCADE)
    class Meta:
        db_table = "commentfrom"
        verbose_name = "评论表"
        verbose_name_plural = verbose_name

