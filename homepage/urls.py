from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.Homepage.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about')

]