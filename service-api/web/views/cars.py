from rest_framework.views import APIView
from web.models import *
from web.serializers.cars import (
    CarsSerializer,
    CarUpdateSerializer,
)
from rest_framework.response import Response
from web.permissions import *

class CarList(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get(self, request, format=None):
        queryset = Cars.objects.all()
        data = CarsSerializer(queryset, many=True).data
        response = {
            "data": data,
            "message": "success"
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = CarUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)
    
class CarDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarsSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarUpdateSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(204)