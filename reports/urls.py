from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost/', views.report_lost, name='report_lost'),
    path('found/', views.report_found, name='report_found'),
]