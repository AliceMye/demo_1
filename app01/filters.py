from django_filters.rest_framework import FilterSet
from . import models


class EmpFilter(FilterSet):
    class Meta:
        model = models.Emp
        fields = ['emp_num']

