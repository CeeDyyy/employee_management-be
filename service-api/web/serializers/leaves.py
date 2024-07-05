from rest_framework import serializers
from web.models import *

class LeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['id', 'user_id', 'detail', 'start_date', 'end_date', 'record_timestamp', 'status', 'approver', 'reason', 'update_timestamp']

class LeavesCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    detail = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Leaves
        fields = ['user_id', 'detail', 'start_date', 'end_date']

class LeavesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['user_id', 'detail', 'start_date', 'end_date']
# อันนี้เป็นตัวอย่างของการ`แยก Create กับ Update ออกจากกัน`(แม้ fields จะเหมือนกันก็ตาม), ซึ่งที่จริงจะทำแบบของ cars ที่เป็นอันเดียวกันก็ได้

class LeavesApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['status', 'approver', 'reason']