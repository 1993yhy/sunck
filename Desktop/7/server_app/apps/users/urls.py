from django.contrib import admin
from django.urls import path,include,re_path
from users.views import SmsCodeViewSet,SubmitPhotoViewSet

from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"codes",SmsCodeViewSet,base_name="codes")
router.register(r"submitphoto",SubmitPhotoViewSet,base_name="submitphoto")

# router.register(r"teacher/pwd",TeacherPwdViewSet,base_name="teacher/pwd")
urlpatterns = [
    # re_path(r'^(?P<version>[v1|v2]+)/course/$', views.CourseView.as_view()),

    # drf自带的token认证模式
    # url(r'api-token-auth/', views.obtain_auth_token),

    #jwt的认证接口
    url(r'login/', obtain_jwt_token),
    url(r'^',include(router.urls)),


    # re_path(r'^(?P<version>[v1|v2]+)/course/$', views.CourseView.as_view({'get': 'list','post':'create'})),
    # re_path(r'^(?P<version>[v1|v2]+)/course/(?P<pk>\d+)/$', views.CourseView.as_view({'get': 'retrieve','delete':'destroy','put':'update','patch':'perform_update'})),
]