from django.contrib import admin
from django.urls import path,include,re_path
from classroom import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"room",views.ClassRoomViewSet,base_name="room")
router.register(r"seacher",views.ClassSeacherViewSet,base_name="seacher")
# router.register(r"tc",views.TeacherViewSet,base_name="tc")
router.register(r"roomlist",views.RoomTestViewSet,base_name="roomlist")
router.register(r"application",views.ApplicationViewSet,base_name="application")
router.register(r"examine",views.ExamineViewSet,base_name="examine")
router.register(r"group",views.GroupViewSet,base_name="group")
router.register(r"fenzu",views.FenZuViewSet,base_name="fenzu")
router.register(r"card",views.CardViewSet,base_name="card")
# router.register(r"times",views.CourseTimesViewSet,base_name="times")
# router.register(r"task",views.TaskViewSet,base_name="task")

urlpatterns = [

    url(r'^',include(router.urls)),
]