
import requests
# from rest_framework import viewsets
# from rest_framework.response import Response
import random
import os
from users.models import StaticPhoto

# def randm_photo():


def randm_photo():
    '''用户随机头像'''
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(BASE_DIR, r"static\touxiang")
    for root, dirs, files in os.walk(static_dir):
        xiabiao = random.randint(0,len(files)-1)
        return files[xiabiao]



def retmessage(code=0, msg='成功', data={}):
    '''
   返回数据报格式
   # @code: 返回码 0 表示成功， 1表示失败
   # @msg 返回信息
   # @data  返回信息
   '''
    return {
        'code':code,
        'msg':msg,
        'data':data
    }

def sendSmsCode(mobile):
    '''发送验证码'''
    base_str = '0123456789'
    str = "[AI Yi Education]Your phone verification code is:"
    code = ''.join(random.sample(base_str, 6))
    sms = requests.get(
        "http://api.smsglobal.com/http-api.php?action=sendsms&user=ayiu11ia&password=dPoSXQB6&from=Test&to=%s&text=%s%s" % (
            mobile, str, code))
    return {code,sms}


# class MyModelViewSet(viewsets.ModelViewSet):
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         is_valid = serializer.is_valid(raise_exception=False)
#         #######
#         if not is_valid:
#             return Response({'code': 1, 'msg': '失败', 'data': serializer.errors})
#         self.perform_update(serializer)
#         ######
#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}
#
#         return Response({'code': 0, 'msg': '成功', 'data': serializer.data})
#
#
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'code': 0, 'msg': '成功', 'data': serializer.data})


