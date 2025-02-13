from django.urls import path
from . import views

urlpatterns = [
    path('', views.milk_shop, name='home'),
    path('members/', views.milk_shop, name='members'),
]
