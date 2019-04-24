from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    url(r'^leads/', include('leads.url')),
]
