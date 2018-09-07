from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class LaptopLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10

class LaptopPageNumberPagination(PageNumberPagination):
    page_size = 12