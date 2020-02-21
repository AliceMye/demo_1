from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
from rest_framework.generics import CreateAPIView

from app01 import serializers
from .response import APIResponse


class RegisterCreate(CreateAPIView):
    # 序列化
    renderer_classes = serializers.RegisterModelSerializer

    # 自定义响应结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()  # 自定入库 需要重写create方法
        headers = self.get_success_headers(serializer.data)

        return APIResponse(0, 'OK',
                           results=serializer.RegisterModelSerializer(user_obj).data,
                           http_status=201,
                           headers=headers)



# 登录
from rest_framework.views import APIView


class LoginAPIView(APIView):
    # 禁用认证与权限组件
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = serializers.LoginModelSerializer(data=request.data)

        user_ser.is_valid(raise_exception=True)
        results = serializers.LoginModelSerializer(user_ser.user)
        print(results)
        #  取出登录用户与token返回给前台
        return APIResponse(token=user_ser.token, results=serializers.LoginModelSerializer(user_ser.user).data)


# 工號 搜索 过滤 分页

from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import models, serializers, paginations


# 分类


class CategoryListAPIView(ListAPIView):
    queryset = models.Emp.objects.filter()
    serializer_class = serializers.CategoryModelSerializer


from rest_framework.filters import OrderingFilter
# 分类：pip install django-filter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmpFilter


class EmpAPIView(ListAPIView, RetrieveAPIView):
    queryset = models.Emp.objects.filter()
    serializer_class = serializers.EmpModelSerializer

    # 分页
    pagination_class = paginations.MyPageNumberPagination

    # 过滤条件们
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'group_name', 'emp_num']
    filter_class = EmpFilter

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:  # 单查
            return self.retrieve(request, *args, **kwargs)
        else:  # 群查
            return self.list(request, *args, **kwargs)


# 可以进行员工分组的字段筛选条件
from django_filters.rest_framework import DjangoFilterBackend


def mes_index(request):
    if request.method == 'POST':
        data = request.POST

        print(data)

        """
         max(iterable, *[, default=obj, key=func]) -> value
         max(arg1, arg2, *args, *[, key=func]) -> value
         default=obj 返回一个对象
         li = [{'name': '小明', 'age': 15},
      {'name': '小红', 'age': 38},
      {'name': '小绿', 'age': 20},
      {'name': '小东', 'age': 25}]

      eg:{'age': 38, 'name': '小红'}
        """

        return HttpResponse(max(data, key=lambda dic: dic['age']))