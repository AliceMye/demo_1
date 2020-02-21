from app01 import celery_task
from rest_framework.generics import CreateAPIView
from models import Emp
from .celery import app
from app01 import views

# from settings.const import BANNER_COUNT
# from home.serializers import BannerModelSerializer
from django.core.cache import cache
from django.conf import settings


@app.task
def insert_emp():
    # 新增加员工 异步任务

    views.RegisterCreate(CreateAPIView)

    # 更新缓存
    return True
