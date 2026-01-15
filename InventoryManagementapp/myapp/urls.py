from django.urls import path, include
from myapp import views

urlpatterns = [
    path('sales/', views.dashboard, name='dashboard'),
    path('', views.index, name='index')
]
