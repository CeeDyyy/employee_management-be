from rest_framework import serializers
# from django.utils.translation import gettext_lazy as _
from django.core.validators  import RegexValidator

# validate_password = RegexValidator(r'^(?=.*[!@#$%^&*\.])^(?=.*[0-9])^(?=.*[A-Za-z\.])[A-Za-z0-9!@#$%^&*\.]{1,20}$',"รูปแบบรหัสไม่ถูกต้อง")
class ImgSerializer(serializers.Serializer):
    img = serializers.FileField(max_length=None, allow_empty_file=False, use_url=True)