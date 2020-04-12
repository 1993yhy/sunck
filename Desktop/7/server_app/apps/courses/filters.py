# -*- coding: utf-8 -*-
__author__ = 'bobby'

# import django_filters
# from django.db.models import Q
#
# from courses.models import CourseManagement
#
# #
# class CourseFilter(django_filters.rest_framework.FilterSet):
#     """
#     课程的过滤类
#     """
#     pricemin = django_filters.NumberFilter(name='shop_price', help_text="最低价格",lookup_expr='gte')
#     pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
#     top_category = django_filters.NumberFilter(method='top_category_filter')
#
#
#     def top_category_filter(self, queryset, name, value):
#         return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
#
#
#     class Meta:
#         model = CourseManagement
#         fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']