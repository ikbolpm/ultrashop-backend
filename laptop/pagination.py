from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class LaptopLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class LaptopPageNumberPagination(PageNumberPagination):
    page_size = 10
