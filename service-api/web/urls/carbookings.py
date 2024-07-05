from django.conf.urls import url, include
from web.views.carbookings import (
    CarBookingList,
    CarBookingDetail,
    CarBookingApproval
)

urlpatterns = [
    url(r'^carbookings/$', CarBookingList.as_view(),name="carbooking-list"),
    url(r'^carbooking/(?P<pk>[0-9]+)/$', CarBookingDetail.as_view(),name="carbooking-detail"),
    url(r'^carbookingapproval/(?P<pk>[0-9]+)/$', CarBookingApproval.as_view(),name="carbooking-approval")
]