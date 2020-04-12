from django.contrib import admin
from django.urls import path,include,re_path
from teacher import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from teacher.views import TeacherRegViewSet,TeacherInfoViewSet,TeacherPwdViewSet,Test

router = DefaultRouter()



router.register(r"reg",TeacherRegViewSet,base_name="reg")
router.register(r"info",TeacherInfoViewSet,base_name="info")
# router.register(r"submitphoto",SubmitPhotoViewSet,base_name="submitphoto")
router.register(r"changepassword",TeacherPwdViewSet,base_name="changepassword")
router.register(r"test",Test,base_name="test")

urlpatterns = [

    # drf自带的token认证模式
    # url(r'api-token-auth/', views.obtain_auth_token),

    url(r'^',include(router.urls)),
    # url(r'^info/$',TeacherInfoViewSet.as_view())

    # url(r'^pwd$',TeacherPwdViewSet.as_view()),
]