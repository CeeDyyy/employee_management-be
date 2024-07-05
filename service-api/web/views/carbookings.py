from rest_framework.views import APIView
from web.models import *
from web.serializers.carbookings import (
    CarBookingsSerializer,
    CarBookingsCreateSerializer,
    CarBookingsUpdateSerializer,
    CarBookingsApprovalSerializer,
)
from rest_framework.response import Response
from web.permissions import *

class CarBookingList(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get(self, request, format=None):
        queryset = CarBookings.objects.all().order_by('id').values() #เรียงตามลำดับเก่าไปใหม่(ถ้าอยากให้เป็นใหม่ไปเก่าให้ใส่('-id')) ถ้าไม่ใส่มันจะเรียงจากอัปเดตล่าสุด
        data = CarBookingsSerializer(queryset, many=True).data
        response = {
            "data": data,
            "message": "success"
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = CarBookingsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)

class CarBookingDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return CarBookings.objects.get(pk=pk)
        except CarBookings.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def get(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsSerializer(carbooking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsUpdateSerializer(carbooking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    def delete(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        carbooking.delete()
        return Response(204)

class CarBookingApproval(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin, PermissionApprover]

    def get_object(self, pk):
        try:
            return CarBookings.objects.get(pk=pk)
        except CarBookings.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def put(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsApprovalSerializer(carbooking, data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
        return Response(serializer.errors, 400)