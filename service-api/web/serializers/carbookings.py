from rest_framework import serializers
from web.models import *

class CarBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookings
        fields = ['id', 'user_id', 'detail', 'start_date', 'end_date', 'car_id', 'record_timestamp', 'status', 'approver', 'reason', 'update_timestamp']

class CarBookingsCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    detail = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)
    car_id = serializers.CharField(required=True)

    class Meta:
        model = CarBookings
        fields = ['user_id', 'detail', 'start_date', 'end_date', 'car_id']

class CarBookingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookings
        fields = ['user_id', 'detail', 'start_date', 'end_date', 'car_id']
# อันนี้เป็นตัวอย่างของการ`แยก Create กับ Update ออกจากกัน`(แม้ fields จะเหมือนกันก็ตาม), ซึ่งที่จริงจะทำแบบของ cars ที่เป็นอันเดียวกันก็ได้

class CarBookingsApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookings
        fields = ['status', 'approver', 'reason']