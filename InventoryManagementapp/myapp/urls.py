from django.urls import path, include

urlpatterns = [
    path('sales/', include('myapp.sales.urls')),
]
