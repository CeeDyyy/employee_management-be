from django.conf.urls import url, include
from web.views.users import (
    UserList,
    UserCheck,
    UserDetail
)

urlpatterns = [
    url(r'^users/$', UserList.as_view(),name="user-list"),
    url(r'^usercheck/$', UserCheck.as_view(),name="user-check"),
    url(r'^user/(?P<pk>\w+)/$', UserDetail.as_view(),name="user-detail")    # รับ string อะไรก็ได้
]