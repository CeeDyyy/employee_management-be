from rest_framework.views import APIView
from web.models import *
from web.serializers.leaves import (
    LeavesSerializer,
    LeavesCreateSerializer,
    LeavesUpdateSerializer,
    LeavesApprovalSerializer,
)
from rest_framework.response import Response
from web.permissions import *

class LeaveList(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get(self, request, format=None):
        queryset = Leaves.objects.all().order_by('id').values() #เรียงตามลำดับเก่าไปใหม่(ถ้าอยากให้เป็นใหม่ไปเก่าให้ใส่('-id')) ถ้าไม่ใส่มันจะเรียงจากอัปเดตล่าสุด
        data = LeavesSerializer(queryset, many=True).data
        response = {
            "data": data,
            "message": "success"
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = LeavesCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)

class LeaveDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Leaves.objects.get(pk=pk)
        except Leaves.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def get(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesSerializer(leave)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesUpdateSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    def delete(self, request, pk, format=None):
        leave = self.get_object(pk)
        leave.delete()
        return Response(204)

class LeaveApproval(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin, PermissionApprover]

    def get_object(self, pk):
        try:
            return Leaves.objects.get(pk=pk)
        except Leaves.DoesNotExist:
            # raise Http404
            return Response("Not found", 404)

    def put(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesApprovalSerializer(leave, data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
        return Response(serializer.errors, 400)