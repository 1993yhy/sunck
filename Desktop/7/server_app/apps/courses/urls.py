from django.contrib import admin
from django.urls import path,include,re_path
from courses import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r"courses",views.CourseViewSet,base_name="courses")
# router.register(r"times",views.CourseTimesViewSet,base_name="times")
# router.register(r"task",views.TaskViewSet,base_name="task")

urlpatterns = [
    # re_path(r'^(?P<version>[v1|v2]+)/course/$', views.CourseView.as_view()),
    url(r'^',include(router.urls)),
    # url(r'', views.CourseView.as_view()),
    # re_path(r'^(?P<version>[v1|v2]+)/course/$', views.CourseView.as_view({'get': 'list','post':'create'})),
    # re_path(r'^(?P<version>[v1|v2]+)/course/(?P<pk>\d+)/$', views.CourseView.as_view({'get': 'retrieve','delete':'destroy','put':'update','patch':'perform_update'})),
]