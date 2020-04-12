# import xadmin
# from xadmin import views
# from courses.models import CourseManagement,Commodity,CourseTimes,TaskList,Course2Commodity
# from users.models import Role
# class BaseSetting(object):
#     """xadmin的基本配置"""
#     enable_themes = True  # 开启主题切换功能
#     use_bootswatch = True
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
#
# class GlobalSettings(object):
#     """xadmin的全局配置"""
#     site_title = "艾易"  # 设置站点标题
#     site_footer = "艾易教育"  # 设置站点的页脚
#     menu_style = "accordion"  # 设置菜单折叠
# xadmin.site.register(views.CommAdminView, GlobalSettings)
#
#
#
# class CourseManagementModelAdmin(object):
#
#     pass
#
# xadmin.site.register(CourseManagement ,CourseManagementModelAdmin)
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