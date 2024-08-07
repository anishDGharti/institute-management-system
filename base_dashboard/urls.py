from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_dashboard, name='base-dashboard'),
]