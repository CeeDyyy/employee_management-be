from rest_framework import serializers
from web.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id', 
            'user_id', 'display_name', 'status_message', 'picture_url', 
            'name_en_first', 'name_en_middle', 'name_en_last', 'name_en_nick',
            'name_local_first', 'name_local_middle', 'name_local_last', 'name_local_nick',
            'description',
            'position', 'section', 'division', 'department', 'branch', 'company', 'rank',
            'role'
            ]

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'user_id', 'display_name', 'status_message', 'picture_url', 
            'role'
            ]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'name_en_first', 'name_en_middle', 'name_en_last', 'name_en_nick',
            'name_local_first', 'name_local_middle', 'name_local_last', 'name_local_nick',
            'description',
            'position', 'section', 'division', 'department', 'branch', 'company', 'rank',
            'role'
            ]
    # ที่ไม่ต้องมี validate เพราะ Serializer นี้ไม่ได้ถูกใช้โดย POST อยู่แล้ว มันถูกใช้โดย PUT ดังนั้น ไม่มี field อะไรที่ต้อง required เลย
    
class UserExistingSerializer(serializers.Serializer):
    userId = serializers.CharField(required=True)
    displayName = serializers.CharField(required=True)
    pictureUrl = serializers.CharField(required=True)
    statusMessage = serializers.CharField(required=False)