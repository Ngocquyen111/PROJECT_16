from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('payment_qr/', views.payment_qr, name='payment_qr'),
    path('vouchers/', views.voucher_list, name='voucher_list'),
    path('voucher/<int:voucher_id>/', views.voucher_detail, name='voucher_detail'),
]
