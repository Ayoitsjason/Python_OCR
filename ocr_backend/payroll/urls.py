from django.urls import path
from payroll import views

app_name = 'payroll'

urlpatterns = [
  path('scan', views.scan, name='scan'),
]