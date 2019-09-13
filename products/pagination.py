from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 1000

class ProductPageNumberPagination(PageNumberPagination):
    page_size = 10
