#
# from django.db import models
# from users.models import Role,UserInfo,Role2Userinfo,AdmInfo,AdmType,AdmType2AdmInfo,AdmPermission
# from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# from django.contrib.contenttypes.models import ContentType
# # Create your models here.
#
# class CourseManagement(models.Model):
#     '''课程'''
#     COURSE_TYPE = (
#         (0, "基础服务"),
#         (1, "拓展活动"),
#         (2, "增值服务"),
#     )
#     id = models.AutoField(primary_key=True,help_text="课程id")
#     course_name = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="课程名字",help_text="课程名字")
#     course_type = models.IntegerField(choices=COURSE_TYPE, verbose_name="课程类型",help_text="课程类型")
#     # category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
#     course_describe = models.CharField(default="",max_length=1024,blank=True,null=True,verbose_name="课程描述",help_text="课程描述")
#     course_price = models.CharField(default="",max_length=1024, verbose_name="课程价格",help_text="课程价格")
#     #单位字段
#     price_unit = models.CharField(default="",max_length=1024, verbose_name="价格单位",help_text="价格单位")
#     is_show_5 = models.BooleanField(verbose_name="是否显示", default=False)
#     created_time = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name="课程创建时间",help_text="课程创建时间")
#     class Meta:
#         unique_together = ('course_name', 'id',)
#         db_table = "course_management"
#         verbose_name = "课程管理"
#         verbose_name_plural = verbose_name
#     @property
#     def c_type(self):
#         """返回课程类型的文本提示"""
#         return self.course_types[self.course_type][1]
#     @property
#     def course_times_num(self):
#         num = len(self.course.filter(is_show_6=0))
#         return num
#
#     # @property
#     # def class_locations(self):
#     #     class_locations_list =self.course.filter(is_show_6=0).values_list("class_locations")
#     #     data = []
#     #     for item in class_locations_list:
#     #         data.append({
#     #             "class_locations_list":
#     #         })
#
# class CourseTimes(models.Model):
#     '''课次'''
#     Site_type = (
#         (0, "online"),
#         (1, "indoor"),
#         (2, "outdoor"),
#     )
#     id = models.AutoField(primary_key=True,help_text="课次id")
#     couse_name = models.ForeignKey(to="CourseManagement",on_delete=models.CASCADE,related_name="course", db_constraint = False, null=True, blank=True,verbose_name="关联课程")
#     course_times_name = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="课次名称",help_text="课次名称")
#     site_type = models.IntegerField(choices=Site_type, verbose_name="场地类型",blank=True,null=True,help_text="场地类型")
#     class_time = models.DateTimeField(auto_now_add=False,blank=True,null=True,verbose_name="上课时间")
#     class_locations = models.CharField(max_length=128, blank=True, null=True, verbose_name="上课地点")
#     is_show_6 = models.BooleanField(verbose_name="是否显示", default=False)
#     created_time = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name="课次创建时间")
#     class Meta:
#         # abstract = True
#         unique_together = ('course_times_name', 'id',)
#         db_table = "course_times"
#         verbose_name = "课次管理"
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return self.course_times_name
#
#     @property
#     def s_type(self):
#         """返回场地类型的文本提示"""
#         return self.Site_type[self.site_type][1]
#
# class TaskList(models.Model):
#     '''任务'''
#     # ManyToManyField(to="AdmInfo", through="AdmType2AdmInfo", through_fields=("admtype", "adminfo"))
#     server_type = models.ManyToManyField(Role,  through="Server2Task", through_fields=("task", "role_type"), verbose_name="服务者类型",help_text="服务者类型")
#     task_description = models.CharField(default="",max_length=1024, blank=True, null=True, verbose_name="任务描述",help_text="任务描述")
#     remuneration = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="报酬", default=0,help_text="报酬")
#     remuneration_unit = models.CharField(default="", max_length=1024, verbose_name="价格单位", help_text="价格单位")
#
#     course_times = models.ForeignKey(to="CourseTimes", on_delete=models.CASCADE, db_constraint=False, null=True,
#                                    blank=True, verbose_name="关联课次")
#     # server_name = models.ManyToManyField(UserInfo, through="UserInfo2Task", through_fields=("task", "name"),
#     #                                      verbose_name="服务者名字")
#     is_show = models.BooleanField(verbose_name="是否显示", default=False)
#     #re任务id
#
#     class Meta:
#         # abstract = True
#         db_table = "task_list"
#         verbose_name = "任务列表"
#         verbose_name_plural = verbose_name
#
# #派单表，id，绑定任务id
# # class Server2Course(models.Model):
# #     '''服务者与任务相关'''
# #     role_type = models.ForeignKey(Role,on_delete=models.CASCADE, null=True, blank=True,verbose_name="角色类型")
# #     task = models.ForeignKey(to="TaskList",on_delete=models.CASCADE, null=True, blank=True,verbose_name="任务相关")
# #     class Meta:
# #         # abstract = True
# #         db_table = "server_type_task"
# #         verbose_name = "任务管理与角色类型"
# #         verbose_name_plural = verbose_name
# class DispathTask(models.Model):
#     '''派单表'''
#     name = models.ForeignKey(UserInfo,on_delete=models.CASCADE, null=True, blank=True,verbose_name="角色名字")
#     task = models.ForeignKey(to="TaskList",on_delete=models.CASCADE, null=True, blank=True,verbose_name="任务相关")
#     class Meta:
#         # abstract = True
#         db_table = "DispathTask"
#         verbose_name = "派单表"
#         verbose_name_plural = verbose_name
#
#
# # class UserInfo2Task(models.Model):
# #     '''任务管理与服务者姓名'''
# #     name = models.ForeignKey(UserInfo,on_delete=models.CASCADE, null=True, blank=True,verbose_name="角色名字")
# #     task = models.ForeignKey(to="TaskList",on_delete=models.CASCADE, null=True, blank=True,verbose_name="任务相关")
# #     class Meta:
# #         # abstract = True
# #         db_table = "server_name_task"
# #         verbose_name = "任务管理与服务者姓名"
# #         verbose_name_plural = verbose_name
#
# class Commodity(models.Model):
#     '''商品信息'''
#     id = models.AutoField(primary_key=True)
#     is_show = models.BooleanField(verbose_name="是否显示", default=False)
#     commodity_name = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="商品名称")
#     commodity_id = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="商品id")
#     course_name = models.ManyToManyField(CourseManagement,  through="Course2Commodity", through_fields=("commodity_name", "course_name"), verbose_name="商品和课程关系")
#
#     class Meta:
#         # abstract = True
#         unique_together = ('commodity_name', 'id',)
#         db_table = "Commodity"
#         verbose_name = "商品信息"
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return self.commodity_name
#
# class Course2Commodity(models.Model):
#     '''商品与课程关系'''
#     commodity_name = models.ForeignKey(Commodity,on_delete=models.CASCADE, null=True, blank=True,default="",verbose_name="商品名id")
#     course_name = models.ForeignKey(to="CourseManagement",on_delete=models.CASCADE, null=True, blank=True,default="",verbose_name="课程名id")
#     created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="创建时间")
#     is_show = models.BooleanField(verbose_name="是否显示", default=False)
#     class Meta:
#         # abstract = True
#         db_table = "course_commodity"
#         verbose_name = "商品与课程关系"
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return self.commodity_name
#
#
# class Order(models.Model):
#     '''订单列表'''
#     id = models.AutoField(primary_key=True)
#     order_id = models.CharField(default="",max_length=128, blank=True, null=True, verbose_name="订单id")
#     created_time = models.DateTimeField(auto_now_add=False,blank=True,null=True,verbose_name="订单创建时间")
#     commodity_name = models.OneToOneField('Commodity', on_delete=models.CASCADE, to_field='id', null=True)
#     server_man = models.ManyToManyField(Role2Userinfo, through="Server2Order",
#                                          through_fields=("orders", "server"), verbose_name="接单人")
#     is_show = models.BooleanField(verbose_name="是否显示", default=False)
#     class Meta:
#         # abstract = True
#         db_table = "order"
#         verbose_name = "订单列表"
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return self.order_id
#
# class Server2Order(models.Model):
#     order_statu = (
#         (0, "未接单"),
#         (1, "接单"),
#     )
#     orders = models.ForeignKey(Order,on_delete=models.CASCADE, null=True, blank=True,default="",verbose_name="订单id")
#     server = models.ForeignKey(Role2Userinfo,on_delete=models.CASCADE, null=True, blank=True,default="",verbose_name="服务者对应的角色id")
#     statu = models.IntegerField(choices=order_statu, verbose_name="接单状态", blank=True, null=True)
#     class Meta:
#         # abstract = True
#         db_table = "Server2Order"
#         verbose_name = "订单列表"
#         verbose_name_plural = verbose_name