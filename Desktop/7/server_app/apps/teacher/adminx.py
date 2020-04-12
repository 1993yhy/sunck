import xadmin
from xadmin import views
from teacher.models import Teachers
#
#
class TeachersModelAdmin(object):
    list_display = ["user", 'name',"teacher_type", "photo"]
    ordering = ['user']

xadmin.site.register(Teachers ,TeachersModelAdmin)
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