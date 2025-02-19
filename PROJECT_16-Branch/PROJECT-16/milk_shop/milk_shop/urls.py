from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('checkout/', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('payment_qr/', views.payment_qr, name='payment_qr'),
    path('vouchers/', views.voucher_list, name='voucher_list'),
    path('voucher/<int:voucher_id>/', views.voucher_detail, name='voucher_detail'),
=======
    path('', views.milk_shop, name='home'),
    path('members/', views.milk_shop, name='members'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
>>>>>>> d5399da (Them code)
]
