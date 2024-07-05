from rest_framework.views import APIView
from rest_framework import status
from web.response import Response
from web.serializers.exam import ImgSerializer
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
# from rest_framework.decorators import (action, detail_route)
from rest_framework.generics import GenericAPIView
from rest_framework import parsers
# @swagger_auto_schema(
#     request_body=ImgSerializer
# )
class ExampleView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    
    serializer_class = ImgSerializer


    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=ImgSerializer)
    # @action(detail=False, methods=['post'])
    # @detail_route(methods=['get', 'post'], parser_classes=(MultiPartParser,))
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(data={"success": "True"})
        return Response(data={'success': "False"}, status=status.HTTP_400_BAD_REQUEST)
            
            