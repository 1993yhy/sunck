from django.contrib import admin
from django.urls import path,include,re_path
from student import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from student.views import StudentPwdViewSet,StudentRegViewSet,StudentInfoViewSet
router = DefaultRouter()



router.register(r"reg",StudentRegViewSet,base_name="reg")
router.register(r"changepassword",StudentPwdViewSet,base_name="changepassword")
router.register(r"info",StudentInfoViewSet,base_name="info")

urlpatterns = [

    # drf自带的token认证模式
    # url(r'api-token-auth/', views.obtain_auth_token),

    url(r'^',include(router.urls)),
    # url(r'^pwd$',StudentPwdViewSet.as_view()),

]