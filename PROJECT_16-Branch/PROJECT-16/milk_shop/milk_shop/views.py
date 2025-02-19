
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, "app_home/article_list.html", {"articles": articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "app_home/article_detail.html", {"article": article})

def checkout(request):
    return render(request, 'milk_shop/checkout.html')

def process_checkout(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST.get('email', '')
        payment_method = request.POST['payment_method']

        if payment_method == "bank_transfer":
            return redirect('payment_qr')  # Chuyển hướng đến trang QR Code
        
        return HttpResponse("Đặt hàng thành công! Nhân viên sẽ liên hệ bạn để xác nhận.")

def payment_qr(request):
    return render(request, 'milk_shop/payment_qr.html')

