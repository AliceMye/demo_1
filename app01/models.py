from django.db import models

# Create your models here.
import uuid

# 看看用户用不用User 自定义 看情况
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=32, null=False, unique=True)
    password = models.CharField(max_length=645, null=False)


class Emp(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=50, null=False, verbose_name='部门编号')
    emp_num = models.CharField(max_length=64, db_index=True, verbose_name='员工编号')

    class Meta:
        db_table = 'demo_user'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group_name


class Org(models.Model):
    name = models.CharField(unique=True, db_index=True, max_length=50)
    # 员工分类
    type = models.CharField(max_length=32,default=None)
    class Meta:
        db_table = 'org_user'
        verbose_name = '组织模型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name