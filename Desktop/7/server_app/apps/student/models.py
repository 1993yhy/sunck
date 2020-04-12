from django.db import models
from users.models import User
from datetime import datetime


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="students", primary_key=True,
                                help_text="学生id")
    name = models.CharField(default="", max_length=128, blank=True, null=True, verbose_name="姓名",help_text="姓名")
    photo = models.ImageField(upload_to="student_photo", blank=True, null=True, max_length=1024, verbose_name="头像",help_text="头像")
    type = models.CharField(max_length=128,blank=True, null=True,default="student")

    class Meta:
        db_table = "students"
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
