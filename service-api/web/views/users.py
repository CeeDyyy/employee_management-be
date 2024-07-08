from rest_framework.views import APIView
from web.models import *
from web.serializers.users import (
    UsersSerializer,
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
            "message": "success"
        }
        return Response(response, 200)

class UserCheck(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = UserExistingSerializer(data=request.data)
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
            serializerData = UsersSerializer(data)
            encoded_jwt = jwt.encode({"user_id": serializerData.data.user_id, "display_name": serializerData.data.display_name, "role": serializerData.data.role}, "secret", algorithm="HS256")
            return Response({"user": serializerData.data, "token": encoded_jwt}, 200)
        return Response(serializer.errors, 400)
    
class UserDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Users.objects.get(user_id = pk)  # pk ในที่นี้ ไม่ได้เกี่ยวอะไรกับ pk ใน model หรือ database แต่มาจากชื่อที่เราตั้ง ซึ่งในที่นี้คือ <pk> ที่อยู่ใน urls/users.py
        except Users.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data, 200)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(204)