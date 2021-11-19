from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    # path('', views.CartView.as_view(), name='summary'),
    path('', views.StaffView.as_view(), name='staff'),
]
