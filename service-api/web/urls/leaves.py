from django.conf.urls import url, include
from web.views.leaves import (
    LeaveList,
    LeaveDetail,
    LeaveApproval
)

urlpatterns = [
    url(r'^leaves/$', LeaveList.as_view(),name="leave-list"),
    url(r'^leave/(?P<pk>[0-9]+)/$', LeaveDetail.as_view(),name="leave-detail"),
    url(r'^leaveapproval/(?P<pk>[0-9]+)/$', LeaveApproval.as_view(),name="leave-approval")
]