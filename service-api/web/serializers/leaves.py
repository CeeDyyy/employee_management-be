from rest_framework import serializers
from web.models import *
from web.serializers.users import *


class LeavesSerializer(serializers.ModelSerializer):
    user = UsersBookingSerializer()

    class Meta:
        model = Leaves
        fields = '__all__'  # เอาทุก field

class LeavesCreateSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    detail = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)


class LeavesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['user_id', 'detail', 'start_date', 'end_date']
# อันนี้เป็นตัวอย่างของการ`แยก Create กับ Update ออกจากกัน`(แม้ fields จะเหมือนกันก็ตาม), ซึ่งที่จริงจะทำแบบของ cars ที่เป็นอันเดียวกันก็ได้

class LeavesApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['status', 'approver', 'reason']