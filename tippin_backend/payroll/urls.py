from django.conf.urls import include
from django.urls import path
from payroll import views

payroll = [
  path('/scans', views.scans, name='payroll_scans'),
]

urlpatterns = [
  path('payroll', include(payroll)),
]