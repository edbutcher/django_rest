# coding=utf-8
from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithMaxLimit(LimitOffsetPagination):
    max_limit = 10