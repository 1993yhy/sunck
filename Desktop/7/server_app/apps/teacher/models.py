from django.db import models
from users.models import User
from datetime import datetime


class Teachers(models.Model):
    '''老师详情表'''
    t_type = (
        ("Dr.", ""),
        ("Mr.", ""),
        ("Miss.", ""),
        ("Mrs.", ""),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teachers", primary_key=True,
                                help_text="老师id")
    name = models.CharField(default="", max_length=128, blank=True, null=True, verbose_name="姓名",help_text="姓名")
    teacher_type = models.CharField(choices=t_type, default="Dr.",max_length=32, verbose_name="老师类型",help_text="老师类型")
    photo= models.ImageField(upload_to="teacher_photo", blank=True, null=True, max_length=1024,verbose_name="头像",help_text="头像")
    class Meta:
        db_table = "teachers"
        verbose_name = "老师信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
    # @property
    # def teacher(self):
    #     """老师和称谓"""
    #     return self.t_type[self.teacher_type][1]+":"+self.name
