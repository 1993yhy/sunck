# from rest_framework import serializers
# from courses import models
# from rest_framework.validators import UniqueValidator
#
#
# class CoursesSerializers(serializers.ModelSerializer):
#
#     created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S',help_text="创建时间")
#     course_type_name = serializers.CharField(source='get_course_type_display',read_only=True)
#     course_name = serializers.CharField(label="课程名称", help_text="课程名称", required=True,allow_blank=True,
#                                         validators=[UniqueValidator(queryset=models.CourseManagement.objects.all(), message="该课程已经存在")])
#     class Meta:
#         model = models.CourseManagement
#         fields = ['id',"course_name","course_type_name","course_type","course_price","course_times_num","created_time","course_describe"]
#         extra_kwargs = {"course_describe": {"write_only": True},
#                         "course_type":{"write_only": True}
#                         }
#
#     # def update(self, instance, validated_data):
#     #     super().update(self, instance, validated_data)
#     #     obj = models.CourseManagement.objects.get("course_name")
#
#
# # class CoursesSerializers2(serializers.ModelSerializer):
# #     created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
# #     course_name = serializers.CharField(read_only=True)
# #     class Meta:
# #         model = models.CourseManagement
# #         fields = ['id',"course_name","course_type","course_price","course_times_num","created_time","course_describe"]
# #         # extra_kwargs = {"course_describe": {"write_only": True},
# #         #                 }
#
# class CourseTimesSerializers(serializers.ModelSerializer):
#     '''新增课次序列化器'''
#     # couse_name = serializers.CharField(source="couse_name",write_only=True )
#     couse_name = serializers.PrimaryKeyRelatedField(required=True,help_text="课程id",queryset=models.CourseManagement.objects.all())
#
#     course_times_name = serializers.CharField(label="课次名称", help_text="课次名称", required=True, allow_blank=True,
#                                         validators=[UniqueValidator(queryset=models.CourseTimes.objects.all(),
#                                                                     message="该课次已经存在")])
#     class Meta:
#         model = models.CourseTimes
#         fields = ["couse_name",'id',"course_times_name","site_type"]
#         extra_kwargs = {"id": {"read_only": True}}
#     # def create(self, validated_data):
#     #     course_id = validated_data["couse_name"]
#     #     course_times_name = validated_data["course_times_name"]
#     #     site_type = validated_data["site_type"]
#
#     # def validate_course_id(self,value):
#     #     print(value)
#     #     ret = {"couse_name":value}
#     #     return ret
# class CourseTimesSerializers2(serializers.ModelSerializer):
#     '''编辑课次等序列化器'''
#
#     course_times_name = serializers.CharField(label="课次名称", help_text="课次名称", required=True, allow_blank=True,
#                                         validators=[UniqueValidator(queryset=models.CourseTimes.objects.all(),
#                                                                     message="该课次已经存在")])
#     class Meta:
#         model = models.CourseTimes
#         fields = ['id',"course_times_name","site_type"]
#
#
# class TaskSerializers(serializers.ModelSerializer):
#     '''任务列化器'''
#     # server_type = serializers.PrimaryKeyRelatedField(required=True, help_text="服务者类型",
#     #                                                 queryset = models.Role.objects.all())
#     course_times = serializers.PrimaryKeyRelatedField(required=True, help_text="课次id",
#                                                     queryset=models.CourseTimes.objects.all())
#     server_type = serializers.PrimaryKeyRelatedField(required=True, help_text="服务者类型",
#                                                     queryset=models.Role.objects.all(),many=True)
#
#
#     class Meta:
#         model = models.TaskList
#         fields = ['id',"task_description","remuneration","course_times","server_type"]
#     '''
#     很重要的测试
#     def create(self, validated_data):
#         task_description = validated_data["task_description"]
#         remuneration = validated_data["remuneration"]
#         course_times = validated_data["course_times"]
#         print(course_times,"***********")
#
#         existed = models.TaskList.objects.create(**validated_data)
#         # existed.save()
#         return existed
#
#     '''
#
#
#
#
#
