from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class User(AbstractUser):
    '''基本用户信息'''
    mobile = models.CharField(max_length=32)
    password = models.CharField(max_length=1024)
    name = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="名字")
    email = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="电子邮箱")
    is_server_man = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    is_adm = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    class Meta:
        db_table = "userinfo"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.mobile



class ServerUser(models.Model):
    '''服务者用户信息'''

    place_type = (
        ("Auckland", "Auckland"),
    )
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name="users",primary_key=True,help_text="关联用户类型")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    first_name = models.CharField(default="", max_length=128, blank=True, null=True, verbose_name="姓氏")
    last_name = models.CharField(default="", max_length=128, blank=True, null=True, verbose_name="名字")
    passport_number = models.CharField(default="", max_length=32, blank=True, null=True, verbose_name="护照号")
    passport_photo = models.ImageField(default="", upload_to="passport_photo", blank=True, null=True, max_length=1024,
                                       verbose_name="护照照片(正面)")
    visa_photo = models.ImageField(default="", upload_to="visa_status", blank=True, null=True, max_length=1024,
                                   verbose_name="签证照片(正面)")
    work_place = models.CharField(default="", choices=place_type, max_length=128, blank=True, null=True,
                                  verbose_name="工作地点")
    address = models.CharField(default="", max_length=128, blank=True, null=True, verbose_name="住址")
    is_show = models.BooleanField(verbose_name="是否显示", default=False)

    class Meta:
        db_table = "service_user"
        verbose_name = "服务者用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Role(models.Model):
    '''角色表详情'''
    id = models.AutoField(primary_key=True)
    role_type = models.CharField( default="",max_length=128, verbose_name="角色类型")
    role_name = models.CharField(default="",max_length=128, verbose_name="角色名")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="roletype",on_delete=models.CASCADE)
    role_describe = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="角色描述")
    user = models.ManyToManyField(to="ServerUser",through="Role2Userinfo",through_fields=("role","userinfo"))
    is_show = models.BooleanField(verbose_name="是否显示", default=False)

    class Meta:
        db_table = "service_role"
        verbose_name = "角色信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.role_name

class Role2Userinfo(models.Model):
    '''角色和用户关系表'''
    state_choices = (
        (0, "under review"),
        (1, "Not pass"),
        (2, "Certified"),
        (3, "Uncertified"),
    )
    role = models.ForeignKey(to="Role",on_delete=models.CASCADE, null=True, blank=True,verbose_name="角色相关")
    userinfo = models.ForeignKey(to="ServerUser",on_delete=models.CASCADE, null=True, blank=True,verbose_name="用户相关")
    application_materials = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="申请材料")
    training_materials = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="培训资料")
    examination_content = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="考试内容")
    role_state = models.IntegerField(choices=state_choices, default=3, verbose_name="认证状态")
    role_no_pass = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="角色未通过审核原因")
    is_show = models.BooleanField(verbose_name="是否显示", default=False)
    class Meta:
        db_table = "service_role_userinfo"
        verbose_name = "角色用户关系"
        verbose_name_plural = verbose_name



class AdmType(models.Model):
    '''管理员类型'''
    role_type = (
        ("auditor","审核人员"),
        ("operator", "运营人员"),
    )

    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True,related_name="admins",help_text="关联管理员类型")
    role_name = models.CharField(default="",choices=role_type, max_length=128, blank=True, null=True, verbose_name="角色类型")
    is_show = models.BooleanField(verbose_name="是否显示", default=False)
    class Meta:
        db_table = "adm_type"
        verbose_name = "管理员类型"
        verbose_name_plural = verbose_name

    @property
    def role_name_display(self):
        return self.get_role_name_display()
    def __str__(self):
        return self.role_name_display

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

class UploadPhoto(models.Model):
    """
    上传图片地址
    """
    photo_url = models.ImageField(upload_to="UploadPhoto", blank=True, null=True, max_length=1024,verbose_name="头像",help_text="头像")

    class Meta:
        verbose_name = "上传图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.photo_url

class StaticPhoto(models.Model):
    """
    静态头像地址
    """
    photo_url = models.ImageField(upload_to="StaticPhoto", blank=True, null=True, max_length=1024,verbose_name="头像",help_text="头像")

    class Meta:
        verbose_name = "静态头像图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.photo_url


class StaticClassPhoto(models.Model):
    """
    静态班级头像地址
    """
    photo_url = models.ImageField(upload_to="StaticPhoto", blank=True, null=True, max_length=1024,verbose_name="头像",help_text="头像")

    class Meta:
        verbose_name = "静态班级图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.photo_url


