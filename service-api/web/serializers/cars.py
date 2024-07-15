from rest_framework import serializers
from web.models import *

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'  # เอาทุก field
    # ข้อมูลที่สามารถ return กลับไปได้

class CarsBookingSerializer(serializers.ModelSerializer):
    thiscar = serializers.SerializerMethodField()
    class Meta:
        model = Cars
        fields = ['thiscar']

    def get_fullname(self, obj):    # get_[ชื่อตัวแปรที่ตั้งไว้ข้างบน] (เป็นประมาณว่า จะให้ fullname ข้างบนมัน return อะไร)
        # return obj.title + obj.license  # ใช้วิธีนี้ไม่ได้ พอข้อมูลเป็น None แล้วมันพัง
        return f"{obj.title} {obj.license}"

class CarUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    capacity = serializers.IntegerField(required=False)
    license = serializers.CharField(required=False)
    # เริ่มต้นรับค่าเข้ามาแบบไม่ required; ซึ่ง default มันคือ True แต่ถ้าเราใช้ ModelSerializer (ในที่นี้ใช้) และตั้ง blank=True หรือ default หรือ null=True ใน Model (ซึ่งอันนี้ใช่) ค่า default จะเป็น False, ซึ่งด้วยความที่เป็นงี้ทำให้ที่จริงแล้วเราไม่ต้องใส่ required=False ก็ได้ (มั้งนะ ไม่แน่ใจ แต่คิดว่าเป็นงั้น)
    class Meta:
        model = Cars
        fields = ['title','type','capacity', 'license']
    # ข้อมูลที่สามารถแก้ได้

    # self มาจาก car ที่ส่งมาจาก view (คือถ้ามันมีส่งมาแปลว่ามันเป็น PUT ถ้าไม่มีส่งมาแปลว่ามันเป็น POST)
    # ซึ่งถ้า self.instance is None แปลว่า self ไม่ได้ถูกส่งมา ซึ่งเป็น POST แล้ว value ดันไม่มี ก็ให้ error. แต่ถ้า self.instance มันไม่ None แปลว่า self ถูกส่งมา ซึ่งเป็น PUT ก็ให้ value ไหลผ่านไป ไปแก้ข้อมูลได้เลย
    def validate_title(self, value):
        if self.instance is None:
            if not value:
                raise serializers.ValidationError("Title is Required.")
        return value

    def validate_type(self, value):
        if self.instance is None:
            if not value:
                raise serializers.ValidationError("Type is Required.")
        return value

    def validate_capacity(self, value):
        if self.instance is None:
            if not value:
                raise serializers.ValidationError("Capacity is Required.")
        return value

    def validate_license(self, value):
        if self.instance is None:
            if not value:
                raise serializers.ValidationError("License is Required.")
        return value
    
# ModelSerializer คือมันต่อตรงกับ model แก้ไขอะไรตรงไปตรงมา (และต้องกำหนด class Meta ด้วย) ส่วน Serialzer เฉย ๆ เราต้องมากำหนดฟีล interface ที่มัน custom เช่น รับตัวแปรนึงมาแล้วมาทำเงื่อนไขซัมติงก่อน 