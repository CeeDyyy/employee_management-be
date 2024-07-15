from rest_framework import serializers
from web.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # เอาทุก field
    # ข้อมูลที่สามารถ return กลับไปได้

class UsersBookingSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    class Meta:
        model = Users
        fields = ['fullname']

    def get_fullname(self, obj):    # get_[ชื่อตัวแปรที่ตั้งไว้ข้างบน] (เป็นประมาณว่า จะให้ fullname ข้างบนมัน return อะไร)
        # return obj.name_local_first + obj.name_local_middle + obj.name_local_last + obj.name_local_nick   # ใช้วิธีนี้ไม่ได้ พอข้อมูลเป็น None แล้วมันพัง
        return f"{obj.name_local_first} {obj.name_local_middle} {obj.name_local_last} {obj.name_local_nick}"

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