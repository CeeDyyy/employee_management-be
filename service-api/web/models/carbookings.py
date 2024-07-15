from django.db import models
from web.models.option import *
import datetime

class CarBookings(models.Model):
    user = models.ForeignKey('Users', related_name='user_carbooking', on_delete=models.CASCADE, default=None) # เป็น foreign key ไปโมเดล Users โดยให้ Users มาที่นี่โดยอ้างอิงว่า user_carbooking ถ้า carbooking ใดโดนลบก็จะลบ carbooking ดังกล่าวด้วย ถ้าไม่มีค่าอะไร default จะเป็น None
    detail = models.CharField(max_length=512, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    car = models.ForeignKey('Cars', related_name='car_booking', on_delete=models.CASCADE, default=None) # เป็น foreign key ไปโมเดล Cars โดยให้ Cars มาที่นี่โดยอ้างอิงว่า car_booking ถ้า car ใดโดนลบก็จะลบ carbooking ดังกล่าวด้วย ถ้าไม่มีค่าอะไร default จะเป็น None
    record_timestamp = models.DateTimeField(null=True, blank=True)  # ใส่ auto_now_add=True ไปในนี้แทน if ใน def save() ข้างล่างก็ได้ ผลลัพธ์คล้าย ๆ กัน จะต่างกันตรงที่ ถ้าใส่ auto_now_add=True ตรงนี้แล้วลบ if ข้างล่าง ตอน Create แทนที่เวลา _timestamp ของ record_ กับ update_ จะตรงกัน เพราะมันสร้างพร้อมกัน แต่กลายเป็นว่า ของ update_ จะเร็วกว่าเสี้ยววิ เพราะมันถูกทำก่อนแล้วใน def save() ส่วนของ record_ จะช้ากว่าเพราะมันถูกทำตรงนี้ ซึ่งเป็นหลังจาก def save() ทำเสร็จแล้ว และนี่เป็นเหตุผลที่ตอนนี้เลือกวิธีให้มันทำใน def save() ไปเลย
    status = models.BooleanField(max_length=8, null=True, blank=True)
    approver = models.CharField(max_length=64, null=True, blank=True)
    reason = models.CharField(max_length=512, null=True, blank=True)
    update_timestamp = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        if self._state.adding:
            self.record_timestamp = now
        self.update_timestamp = now
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s (%s - %s) : %s, %s' % (
            self.user, self.start_date, self.end_date, self.status, self.approver
            )