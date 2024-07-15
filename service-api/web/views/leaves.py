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
        queryset = Leaves.objects.all().order_by('id') #เรียงตามลำดับเก่าไปใหม่(ถ้าอยากให้เป็นใหม่ไปเก่าให้ใส่('-id')) ถ้าไม่ใส่มันจะเรียงจากอัปเดตล่าสุด
        data = LeavesSerializer(queryset, many=True).data
        response = {
            "data": data,
            "detail": "success",
            "status": True
        }
        return Response(response, 200)

    def post(self, request, format=None):
        serializer = LeavesCreateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            detail = serializer.validated_data['detail']
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']

            user = Users.objects.get(user_id=user_id)

            Leaves.objects.create(
                user = user,
                detail = detail,
                start_date = start_date,
                end_date = end_date
                
                )
            return Response({"data": serializer.data, "detail": "Leaving Added!", "status": True}, 201)
        return Response({"data": serializer.errors, "detail": "Failed to Add Leaving!", "status": False}, 400)

class LeaveDetail(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin]

    def get_object(self, pk):
        try:
            return Leaves.objects.get(pk=pk)
        except Leaves.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def get(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesSerializer(leave)
        return Response({"data": serializer.data, "detail": "Success", "status": True}, 200)

    def put(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesUpdateSerializer(leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "detail": "Leaving Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update Leaving!", "status": False}, 400)

    def delete(self, request, pk, format=None):
        leave = self.get_object(pk)
        leave.delete()
        return Response({"detail": "Leaving Deleted!", "status": True}, 200)

class LeaveApproval(APIView):
    authentication_classes = []
    permission_classes = [PermissionIsLogin, PermissionApprover]

    def get_object(self, pk):
        try:
            return Leaves.objects.get(pk=pk)
        except Leaves.DoesNotExist:
            # raise Http404
            return Response({"detail": "Not found", "status": False}, 404)

    def put(self, request, pk, format=None):
        leave = self.get_object(pk)
        serializer = LeavesApprovalSerializer(leave, data=request.data)
        if serializer.is_valid():
               serializer.save()
               return Response({"data": serializer.data, "detail": "Leaving Approval Updated!", "status": True}, 200)
        return Response({"data": serializer.errors, "detail": "Failed to Update Leaving Approval!", "status": False}, 400)