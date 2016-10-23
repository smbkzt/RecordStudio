from django.conf.urls import url, include
from django.contrib import admin

from emailer import views

urlpatterns = [
    url(r'^', include('bookings.urls'), name='booking'),
    url(r'^send/', views.EmailTest.send, name='emailer'),
    url(r'^accounts/', include('accounts.urls'), name='acc'),
    url(r'^admin/', admin.site.urls),
    url(r'^bookings/', include('bookings.urls'))

]
