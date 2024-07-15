from rest_framework import serializers
from web.models import *
from web.serializers.users import *
from web.serializers.cars import *

class CarBookingsSerializer(serializers.ModelSerializer):
    user = UsersBookingSerializer()
    car = CarsBookingSerializer()
    class Meta:
        model = CarBookings
        fields = '__all__'

class CarBookingsCreateSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    detail = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)
    car_id = serializers.CharField(required=True)

class CarBookingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookings
        fields = ['user_id', 'detail', 'start_date', 'end_date', 'car_id']
# อันนี้เป็นตัวอย่างของการ`แยก Create กับ Update ออกจากกัน`(แม้ fields จะเหมือนกันก็ตาม), ซึ่งที่จริงจะทำแบบของ cars ที่เป็นอันเดียวกันก็ได้

class CarBookingsApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookings
        fields = ['status', 'approver', 'reason']