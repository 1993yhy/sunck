"""server_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

import xadmin
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title='接口文档')),
    # url(r'^login/', obtain_jwt_token),
    # url(r"courses/", views.CourseView.as_view()),
    url(r"^api/", include("courses.urls")),
    url(r"^api/users/", include("users.urls")),
    url(r"^api/teacher/", include("teacher.urls")),
    url(r"^api/student/", include("student.urls")),
    url(r"^api/classroom/", include("classroom.urls")),

#视图集
    # url(r"courses/", views.CourseViewset.as_view({"get":"list","post":"create"})),
    # url(r"courses/(?P<pk>\d+)/$",views.CourseViewset.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]
