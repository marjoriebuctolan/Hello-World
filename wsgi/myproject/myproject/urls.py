from django.conf.urls import include, url
from django.contrib import admin
from hiworld.views import helloWorld

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hiworld/', helloWorld),
]
