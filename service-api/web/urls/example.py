from django.conf.urls import url
from web.views.example import ExampleView

urlpatterns = [
    url(r'^v1/example/$', ExampleView.as_view(),name="example-view"),
]