from django.shortcuts import render
from rest_framework.generics import mixins,GenericAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.db.models import Q

from utils.permissions import IsOwnerOrReadOnly,MyPermission1,MyPermission2
from classroom.serializers import ClassRoomSerializer,ClassSeacherSerializer,ClassInfoSerializer,ApplicationSerializer,ApplicationSerializer1,GroupSerializer,FenZuSerializer,RemoveMemberSerializer,CardSerializer
from classroom.models import ClassRoom,ClassMember,ClassGroup,Card
from teacher.models import Teachers
from utils.common import retmessage
from utils.verifyclass import Verify_args

class ClassRoomViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    '''
    list:
        查看自己所在的班级
    create:
        创建班级
    destroy:
        删除班级
    '''
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly,MyPermission1)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()
    def get_queryset(self):
        return ClassRoom.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room_name = serializer.validated_data["room_name"]
        # ClassRoom.objects.get_or_create()
        grade = serializer.validated_data["grade"]
        if Verify_args.class_create_check(room_name,grade):
            return Response(Verify_args.class_create_check(room_name,grade))
        self.perform_create(serializer)
        #创建教室成员信息
        # print(serializer.data)
        ClassMember.objects.create(user_id=self.request.user.id,member_type="teacher",application_type ="creater",class_id_id=serializer.data["id"],examine_man_id=self.request.user.id,status="inclass",application_result=1)

        return Response(retmessage(0,"创建班级成功",data=serializer.data), status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(retmessage(0,"删除教室成功"), status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

class ClassSeacherViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    list:
        搜索班级号
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = "room_num"
    def list(self, request, *args, **kwargs):
        room_num = self.request.query_params.get("room_num")
        print(room_num)
        queryset = self.filter_queryset(self.get_queryset().filter(room_num=room_num))
        serializer = self.get_serializer(queryset, many=True)
        if not ClassRoom.objects.filter(room_num=room_num):
            return Response(retmessage(1, "搜索教室号不存在", data=serializer.data),status=status.HTTP_400_BAD_REQUEST)
        return Response(retmessage(0, "搜索教室", data=serializer.data),status=status.HTTP_200_OK)

# class TeacherViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
#     '''
#     list:
#         搜索班级号
#     '''
#     # permission_classes = (IsAuthenticated,)
#     # authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
#     serializer_class = TeacherSerializer
#     queryset = Teachers.objects.all()
#     class 加入班级:
#           班级id


class RoomTestViewSet(mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    '''
    list:
    展示教室列表及人数
    destroy:
    移出成员或退出教室
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ClassInfoSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return ClassInfoSerializer
        return RemoveMemberSerializer
    def get_queryset(self):
        # print(self.request.user.id)
        if self.action == "list":
        #之查看自己所在的教室
            return ClassRoom.objects.filter(clsroom__user_id=self.request.user.id,clsroom__status="inclass")
        print(self.kwargs["pk"])
        return ClassMember.objects.filter(id=self.kwargs["pk"])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(retmessage(0, "查看教室", data=serializer.data), status=status.HTTP_200_OK)
    def destroy(self, request, *args, **kwargs):
        print(self.get_object().user_id,"xxxxxxxxxx")


        # if self.kwargs["id"] == self.request.user.id:
        instance = self.get_object()
        # self.perform_destroy(instance)
        if instance.user_id == self.request.user.id:
            self.perform_destroy(instance)
            return Response(retmessage(0,"退出教室成功"),status=status.HTTP_200_OK)
        obj = ClassMember.objects.filter(class_id_id=instance.class_id_id).values("examine_man_id")[0]
        if self.request.user.id == obj["examine_man_id"]:
            print(obj["examine_man_id"])
            self.perform_destroy(instance)
            return Response(retmessage(0, "删除成员成功"), status=status.HTTP_200_OK)
        return Response(retmessage(1, "无操作权限"), status=status.HTTP_400_BAD_REQUEST)


        # ClassMember.objects.filter(class_id_id=self)
        # if ClassRoom.objects.filter(user_id=):
        # if self.request.user.id == ClassRoom.objects.filter(clsroom__user_id=self.request.user.id,clsroom__status="inclass")[0].ex

    def perform_destroy(self, instance):
        instance.delete()


class ApplicationViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    '''
    create:
        申请进入教室
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    serializer_class = ApplicationSerializer1
    queryset = ClassMember.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(request.data["Inviter"],"++++++++++")
        print(self.request.user.id)
        member_type = ''
        # class_id = serializer.validated_data["class_id"]
        class_id = request.data["class_id"]
        print(class_id,type(class_id))
        if self.request.user.is_student:
            member_type = "student"
        elif self.request.user.is_teacher:
            member_type = "teacher"
        if ClassMember.objects.filter(user_id=self.request.user.id,status = "inclass",class_id_id=class_id):
            return Response(retmessage(1, "无需审核，已在教室..."), status=status.HTTP_400_BAD_REQUEST)
        try:
            if request.data["Inviter"]:
                if ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id, application_result=3):
                    return Response(retmessage(1, "正在审核中，请耐心等待..."), status=status.HTTP_400_BAD_REQUEST)
                elif ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id, application_result=2):
                    ClassMember.objects.create(user_id=self.request.user.id, class_id_id=request.data["class_id"],
                                               application_type=request.data["application_type"],
                                               member_type=member_type, status="outclass",Inviter_id=request.data["Inviter"])
                    return Response(retmessage(0, "提交申请成功"), status=status.HTTP_200_OK)
                elif ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id, application_result=1):
                    return Response(retmessage(1, "无需审核，已在教室..."), status=status.HTTP_400_BAD_REQUEST)
                # ClassMember.objects.update_or_create(user_id=self.request.user.id,class_id_id = request.data["class_id"],defaults={"application_type":request.data["application_type"],"Inviter_id":request.data["Inviter"],"member_type":member_type,"status":"outclass"})
                ClassMember.objects.create(user_id=self.request.user.id, class_id_id=request.data["class_id"],
                                           application_type=request.data["application_type"],
                                           member_type=member_type, status="outclass",
                                           Inviter_id=request.data["Inviter"])
                return Response(retmessage(0,"提交申请成功"), status=status.HTTP_200_OK)
        except:
            if ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id,application_result=3):
                return Response(retmessage(1, "正在审核中，请耐心等待..."), status=status.HTTP_400_BAD_REQUEST)
            elif ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id,application_result=2):
                ClassMember.objects.create(user_id=self.request.user.id,class_id_id = request.data["class_id"],application_type=request.data["application_type"],member_type=member_type,status="outclass")
                return Response(retmessage(0, "提交申请成功"), status=status.HTTP_200_OK)
            elif ClassMember.objects.filter(user_id=self.request.user.id,class_id_id=class_id,application_result=1):
                return Response(retmessage(1, "无需审核，已在教室..."), status=status.HTTP_400_BAD_REQUEST)
            ClassMember.objects.create(user_id=self.request.user.id, class_id_id=request.data["class_id"],
                                       application_type=request.data["application_type"], member_type=member_type,
                                       status="outclass")
            # ClassMember.objects.update_or_create(user_id=self.request.user.id,class_id_id = request.data["class_id"],
            #                                          defaults={"application_type": request.data["application_type"],
            #                                                    "member_type": member_type, "status": "outclass"})
            return Response(retmessage(0, "提交申请成功"),status=status.HTTP_200_OK)

class ExamineViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    retrieve:
        审核列表展示
    update:
        提交审核结果
    '''
    permission_classes = (IsAuthenticated,MyPermission2)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ApplicationSerializer
    lookup_field = "class_id"

    def get_queryset(self):
        print(self.request.user.id)
        return ClassMember.objects.all()
    def retrieve(self, request, *args, **kwargs):
        print(self.kwargs,"xxxxxxxxxxxx")
        # instance = self.filter_queryset(self.get_queryset().filter(~Q(application_result=2),class_id_id=self.kwargs["class_id"],status="outclass"))
        instance = self.filter_queryset(
            self.get_queryset().filter(class_id_id=self.kwargs["class_id"]))
        data = []
        # for i in instance:
        serializer = self.get_serializer(instance,many = True)
        #     data.append(serializer.data)
        return Response(retmessage(0,"成功",serializer.data),status = status.HTTP_200_OK)
    # def list(self, request, *args, **kwargs):
    #     #过滤出老师所在教室的所有班级id
    #     obj = ClassMember.objects.filter(examine_man_id=self.request.user.id).values("class_id_id")
    #     queryset = []
    #     data = []
    #     class_id_list = []
    #     for item in obj:
    #         class_id_list.append(item["class_id_id"])
    #     class_id_list = list(set(class_id_list))
    #     print(class_id_list)
    #         # ClassMember.objects.filter(class_id_id=item["class_id_id"])
    #     for i in class_id_list:
    #         queryset = self.filter_queryset(self.get_queryset().filter(~Q(application_result=2),class_id_id=i,status="outclass"))
    #         serializer = self.get_serializer(queryset, many=True)
    #         print(serializer.data)
    #         if serializer.data:
    #             data.append(serializer.data)
    #     return Response(retmessage(0, "查看教室", data=data), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # print(type(id),type(application_result))
        try:
            if serializer.validated_data["id"] and serializer.validated_data["application_result"]:
                id = serializer.validated_data["id"]
                application_result = serializer.validated_data["application_result"]
                obj = ClassMember.objects.filter(application_result=3,class_id_id=self.kwargs["class_id"],status="outclass").values("id")
                print(obj)
                id_list = []
                for item in obj:
                    print(item,"aaaaaaaaa")
                    id_list.append(item["id"])
                print(id_list,"xxxxxxxxxxxx")
                if int(id) not in id_list:
                    return Response(retmessage(1,"无权操作"),status = status.HTTP_400_BAD_REQUEST)
                class_member = ClassMember.objects.filter(id = id)[0]
                class_member.application_result = application_result
                if application_result == 1:
                    class_member.status = "inclass"
                class_member.save()

                return Response(retmessage(1,"成功"),status = status.HTTP_200_OK)
        except:

            if ClassMember.objects.filter(examine_man_id=self.request.user.id,class_id_id=self.kwargs["class_id"]):
                obj1 = ClassMember.objects.filter(application_result=3, class_id_id=self.kwargs["class_id"],
                                                  status="outclass")
                for i in obj1:
                    i.status = "inclass"
                    i.application_result = 1
                    i.save()
                return Response(retmessage(0,"一键通过成功"),status = status.HTTP_200_OK)
            else:
                return Response(retmessage(1,"不是自己创建的班级无权操作"),status=status.HTTP_400_BAD_REQUEST)

    #     print(kwargs,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #
    #     if not ClassMember.objects.filter(id = kwargs['id'],examine_man_id=self.request.user.id):
    #         return Response(retmessage(1,"无修改权限"),status=status.HTTP_400_BAD_REQUEST)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #     # print(serializer.data['id'],"xxxxxxxxxxxxxxxxxx")
    #     obj = ClassMember.objects.filter(id =serializer.data['id'])[0]
    #     if obj.application_result == 1:
    #         obj.status = "inclass"
    #         obj.save()
    #     return Response(retmessage(0,"成功"), status=status.HTTP_200_OK)
    # def perform_update(self, serializer):
    #     serializer.save()
    #     print(serializer,"xxxxxxxxxxxxxxxxxx")

class GroupViewSet(mixins.UpdateModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, MyPermission1)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GroupSerializer
    def get_queryset(self):
        return ClassMember.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)


        return Response(retmessage(0,"成功"), status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()


class FenZuViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    '''
    retrieve:
        查看班级成员分组
    update:
        提交分组结果
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = FenZuSerializer
    lookup_field = "class_id"

    def get_queryset(self):
        print(self.request.user.id)
        return ClassMember.objects.all()

    def retrieve(self, request, *args, **kwargs):
        print(self.kwargs, "xxxxxxxxxxxx")
        # instance = self.filter_queryset(self.get_queryset().filter(~Q(application_result=2),class_id_id=self.kwargs["class_id"],status="outclass"))
        instance = self.filter_queryset(
            self.get_queryset().filter(class_id_id=self.kwargs["class_id"],status="inclass"))
        user_id_list = []
        user = ClassMember.objects.filter(class_id_id=self.kwargs["class_id"],status="inclass").values_list("user_id")
        for i in user:
            user_id_list.append(i[0])
        # print(user_id_list,"111111111")
        if self.request.user.id not in user_id_list:
            return Response(retmessage(1, "无访问权限"), status=status.HTTP_400_BAD_REQUEST)
        data = {}
        data["teacher"] = []
        data["student"] = []
        # for i in instance:
        serializer = self.get_serializer(instance, many=True)
        #     data.append(serializer.data)
        for item in serializer.data:
            print(item["user_type"],"xxxxxxxxxx")
            # print(serializer.data)
            if item["user_type"] == "teacher":
                data["teacher"].append(item)
            else:
                data["student"].append(item)
        print(data)
        return Response(retmessage(0, "成功", data=data), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # print(type(id),type(application_result))
        #判断使用者是否有分组权限
        user_permission = ClassMember.objects.filter(examine_man_id=self.request.user.id,class_id_id=self.kwargs["class_id"])
        if not user_permission:
            return Response(retmessage(1,"无分组权限"),status=status.HTTP_400_BAD_REQUEST)
        id = request.data["id"]
        group = request.data["group"]
        if not ClassMember.objects.filter(id=id,class_id_id=self.kwargs["class_id"]):
            return Response(retmessage(1, "输入的班级或id不存在"), status=status.HTTP_400_BAD_REQUEST)
        if ClassMember.objects.filter(id=id,member_type="teacher",status="inclass"):
            return Response(retmessage(1,"无须分组"),status=status.HTTP_400_BAD_REQUEST)
        if not group.isdigit():
            return Response(retmessage(1, "输入不合法"), status=status.HTTP_400_BAD_REQUEST)
        if int(group)>9 or int(group)<0:
            return Response(retmessage(1,"不存在的组别"),status=status.HTTP_400_BAD_REQUEST)
        obj = ClassMember.objects.filter(id = id)[0]
        obj.group = group
        obj.save()
        return Response(retmessage(0,"分组成功"),status=status.HTTP_200_OK)

###########################################分割线#################################################

class CardViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    '''
    list:
        查看卡片列表
    create:
        创建卡片
    update:
        更新卡片
    destroy:
        删除卡片
    '''
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    lookup_field = "id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

















