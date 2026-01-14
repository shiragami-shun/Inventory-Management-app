from django.urls import path
from django.contrib import admin
from .views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('admin/', admin.site.urls),
]
