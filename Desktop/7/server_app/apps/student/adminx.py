import xadmin
from xadmin import views
from classroom.models import ClassRoom,ClassMember,ClassGroup
from student.models import Student

#
#
#
class StudentModelAdmin(object):

    list_display = ["user", 'name', "photo"]
    ordering = ['user']

xadmin.site.register(Student ,StudentModelAdmin)
#
# class CommodityModelAdmin(object):
#
#     pass
#
# xadmin.site.register(Commodity ,CommodityModelAdmin)
#
# class CourseTimesModelAdmin(object):
#
#     pass
#
# xadmin.site.register(CourseTimes ,CourseTimesModelAdmin)
#
# class Course2CommodityModelAdmin(object):
#
#     pass
#
# xadmin.site.register(Course2Commodity ,Course2CommodityModelAdmin)
#
# class TaskListModelAdmin(object):
#
#     pass
#
# xadmin.site.register(TaskList ,TaskListModelAdmin)
#
#
# class RoleModelAdmin(object):
#
#     pass
#
# xadmin.site.register(Role ,RoleModelAdmin)