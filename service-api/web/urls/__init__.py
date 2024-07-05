from web.urls.example import urlpatterns as example
from web.urls.cars import urlpatterns as cars
from web.urls.users import urlpatterns as users
from web.urls.carbookings import urlpatterns as carbookings
from web.urls.leaves import urlpatterns as leaves

urlpatterns = []
urlpatterns += example
urlpatterns += cars
urlpatterns += users
urlpatterns += carbookings
urlpatterns += leaves