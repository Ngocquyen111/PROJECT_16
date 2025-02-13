from django.urls import path
from . import views

urlpatterns = [
    path('', views.milkshop, name='home'),
    path('members/', views.milkshop, name='members'),
]
