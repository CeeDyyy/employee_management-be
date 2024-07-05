from django.conf.urls import url, include
from web.views.cars import (
    CarList,
    CarDetail
)

urlpatterns = [
    url(r'^cars/$', CarList.as_view(),name="car-list"),
    url(r'^car/(?P<pk>[0-9]+)/$', CarDetail.as_view(),name="car-detail")
]