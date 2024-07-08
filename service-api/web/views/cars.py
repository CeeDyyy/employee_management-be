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
            "detail": "success",
            "status": True
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = CarUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "detail": "Car Added!", "status": True}, 201)
        return Response({"data": serializer.errors, "detail": "Failed to Add Car!", "status": False}, 400)
    
class CarDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarsSerializer(car)
        return Response({"data": serializer.data, "detail": "Success", "status": True}, 200)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarUpdateSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "detail": "Car Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update Car!", "status": False}, 400)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response({"detail": "Car Deleted!", "status": True}, 200)