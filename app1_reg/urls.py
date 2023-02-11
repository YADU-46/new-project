from django.contrib import admin
from django.urls import path, re_path, include
from app1_reg import views
urlpatterns = [
    re_path(r'^$', views.home,name ='home'),
    re_path(r"^reg", views.reg, name='reg'),
    re_path(r'^report', views.report, name='report'),
    ]