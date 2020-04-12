import xadmin
from xadmin import views
from classroom.models import ClassRoom,ClassMember,ClassGroup
from users.models import Role
class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "艾易"  # 设置站点标题
    site_footer = "艾易教育"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
xadmin.site.register(views.CommAdminView, GlobalSettings)
#
#
#
class ClassRoomManagementModelAdmin(object):
    list_display = ["id","user", "room_num", 'room_name', 'school', "grade"]
    ordering = ['id']

xadmin.site.register(ClassRoom ,ClassRoomManagementModelAdmin)
#
class ClassMemberModelAdmin(object):
    list_display = ["id",'class_id',"user", 'member_type', "application_time","application_type","application_result","Inviter","status","group"]
    ordering = ['id']


xadmin.site.register(ClassMember ,ClassMemberModelAdmin)
#
# class ClassExamineModelAdmin(object):
#     list_display = ["id", 'examine_man', "application_man", 'examine_result', 'examine_time']
#     ordering = ['id']
#
# xadmin.site.register(ClassExamine ,ClassExamineModelAdmin)
#
class ClassGroupModelAdmin(object):

    list_display = ["id", 'class_id', "members", 'group', 'group_num']
    ordering = ['id']

xadmin.site.register(ClassGroup ,ClassGroupModelAdmin)
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