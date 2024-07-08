from rest_framework.views import APIView
from web.models import *
from web.serializers.users import (
    UsersSerializer,
    TokenSerializer,
    UserExistingSerializer,
    UserUpdateSerializer,
)
from rest_framework.response import Response
from web.permissions import *
import jwt

class UserList(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get(self, request, format=None):
        queryset = Users.objects.all()
        data = UsersSerializer(queryset, many=True).data
        response = {
            "data": data,
            "detail": "success",
            "status": True
        }
        return Response(response, 200)

class UserCheck(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = UserExistingSerializer(data=request.data)  # ตรงนี้ไม่ได้เช็คว่ามี account ไหม แต่เช็คว่า data ที่ได้มามันตาม format ของ serializer นี้ไหม
        if serializer.is_valid():
            userId = serializer.validated_data['userId']
            displayName = serializer.validated_data['displayName']
            pictureUrl = serializer.validated_data['pictureUrl']
            statusMessage = serializer.validated_data['statusMessage']
            try:
                data = Users.objects.get(user_id=userId)
            except Users.DoesNotExist:
                data = Users.objects.create(
                    user_id = userId,
                    display_name = displayName,
                    picture_url = pictureUrl,
                    status_message = statusMessage
                    )
            serializerData = TokenSerializer(data)
            encoded_jwt = jwt.encode(serializerData.data, "secret", algorithm="HS256")
            return Response({"data": encoded_jwt, "detail": "Success", "status": True}, 200)
        return Response({"detail": serializer.errors, "status": False}, 400)
    
class UserDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Users.objects.get(user_id = pk)  # pk ในที่นี้ ไม่ได้เกี่ยวอะไรกับ pk ใน model หรือ database แต่มาจากชื่อที่เราตั้ง ซึ่งในที่นี้คือ <pk> ที่อยู่ใน urls/users.py
        except Users.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        return Response({"data": serializer.data, "detail": "Success", "status": True}, 200)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "detail": "User Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update User!", "status": False}, 400)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response({"detail": "User Deleted!", "status": True}, 200)