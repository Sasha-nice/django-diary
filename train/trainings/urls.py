from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import show_all

urlpatterns = [
    path('', show_all),
]
