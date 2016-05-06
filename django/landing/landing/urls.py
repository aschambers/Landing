from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
  url(r'^', include('apps.landing.urls')), # we inserted this line!!!
  url(r'admin/', include(admin.site.urls)),
]