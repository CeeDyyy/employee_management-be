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
        queryset = CarBookings.objects.all().order_by('id') #เรียงตามลำดับเก่าไปใหม่(ถ้าอยากให้เป็นใหม่ไปเก่าให้ใส่('-id')) ถ้าไม่ใส่มันจะเรียงจากอัปเดตล่าสุด
        data = CarBookingsSerializer(queryset, many=True).data
        response = {
            "data": data,
            "detail": "success",
            "status": True
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = CarBookingsCreateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            detail = serializer.validated_data['detail']
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            car_id = serializer.validated_data['car_id']
            user = Users.objects.get(user_id=user_id)
            car = Cars.objects.get(car_id=car_id)
            CarBookings.objects.create(
                user = user,
                detail = detail,
                start_date = start_date,
                end_date = end_date,
                car = car
                )
            return Response({"data": serializer.data, "detail": "Car Booked", "status": True}, 201)
        return Response({"data": serializer.errors, "detail": "Failed to Book Car", "status": False}, 400)

class CarBookingDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return CarBookings.objects.get(pk=pk)
        except CarBookings.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def get(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsSerializer(carbooking)
        return Response({"data": serializer.data, "detail": "Success", "status": True}, 200)

    def put(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsUpdateSerializer(carbooking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "detail": "Car Booking Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update Car Booking!", "status": False}, 400)

    def delete(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        carbooking.delete()
        return Response({"detail": "Car Booking Deleted!", "status": True}, 200)

class CarBookingApproval(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin, PermissionApprover]

    def get_object(self, pk):
        try:
            return CarBookings.objects.get(pk=pk)
        except CarBookings.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def put(self, request, pk, format=None):
        carbooking = self.get_object(pk)
        serializer = CarBookingsApprovalSerializer(carbooking, data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response({"data": serializer.data, "detail": "Car Booking Approval Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update Car Booking Approval!", "status": False}, 400)