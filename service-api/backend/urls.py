"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

admin.site.site_header = "SERVICE Admin"
admin.site.site_title = "SERVICE Portal"
admin.site.index_title = "Welcome to Low Delay Streaming Portal"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^django-rq/', include('django_rq.urls')),
    
    url(r'^api/', include('web.urls')),
    # url(r'', include('web.urls_template')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^swagger/$', schema_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

