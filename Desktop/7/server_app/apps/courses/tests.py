from django.test import TestCase

# Create your tests here.
    # def get(self, request):
    #     print(request.user)
    #     return self.list(request)
    #
    # def post(self, request):
    #     return self.create(request)
    # def get(self,request,*args,**kwargs):
    #     '''课程展示'''
    #     ret = {"statu":200,"data":""}
    #     course_list = models.CourseManagement.objects.all()
    #     pg = PageNumberPagination()
    #     pager_roles = pg.paginate_queryset(queryset=course_list,request=request,view=self)
    #     ser = CoursesSerializers(instance=pager_roles,many=True)
    #     ret["data"] = ser.data
    #     # return Response(ret)
    #     return pg.get_paginated_response(ret)
    # def post(self,request,*args,**kwargs):
    #     '''添加数据'''
    #     # 接受post请求数据
    #     data_dict = request.data
    #     # 调用序列化器
    #     serializer = Courses2Serializers(data=data_dict)
    #     # 验证
    #     # serializer.is_valid(raise_exception=True)
    #     # 反序列化，保存数据
    #     # serializer.save()
    #     # 响应数据
    #     return Response(serializer.data)


# class CourseView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
#     queryset = models.CourseManagement.objects.all()
#     serializer_class = CoursesSerializers
#     def get(self,request):
#         return self.list(request)
# class CourseViewset(CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     用户
#     """
#     serializer_class = CoursesSerializers
#     queryset = models.CourseManagement.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return CoursesSerializers
#         elif self.action == "create":
#             return Courses2Serializers
#
#         return CoursesSerializers
#
#     # permission_classes = (permissions.IsAuthenticated, )
#     # def get_permissions(self):
#     #     if self.action == "retrieve":
#     #         return [permissions.IsAuthenticated()]
#     #     elif self.action == "create":
#     #         return []
#     #
#     #     return []
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#
#         re_dict = serializer.data
#         payload = jwt_payload_handler(user)
#         re_dict["token"] = jwt_encode_handler(payload)
#         re_dict["name"] = user.name if user.name else user.username
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
#
#     def get_object(self):
#         return self.request.user
#
#     def perform_create(self, serializer):
#         return serializer.save()