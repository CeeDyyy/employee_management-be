from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class Pagination(PageNumberPagination):

    # page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        page = self.request.query_params.get('page', 1)
        if page is not None:
            return Response({
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
                'results': data
            })
        else:
            return Response(data)
    
    def get_page_size(self, request):
        page_size = request.query_params.get('page_size', None)
        try:
            if page_size is not None and int(page_size) > 0:
                return page_size
            else:
                return self.max_page_size

            page = request.query_params.get('page', None)
            if page is not None:
                return 20
            else:
                return self.max_page_size
        except:
            return self.max_page_size