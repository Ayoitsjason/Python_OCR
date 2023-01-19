from django.conf.urls import include
from django.urls import path
from payroll import views

payroll = [
  path('/scan', views.scan, name='payrolls_scans'),
]

urlpatterns = [
  path('payroll', include(payroll)),
]