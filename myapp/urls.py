from django.urls import path
from myapp import views

urlpatterns = [
    path('sales/', views.dashboard, name='dashboard'),
    path('', views.index, name='index'),
]
