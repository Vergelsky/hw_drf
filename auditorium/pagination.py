from rest_framework.pagination import PageNumberPagination


class PageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100
