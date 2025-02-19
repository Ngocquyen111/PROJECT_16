
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import CheckoutForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, "app_home/article_list.html", {"articles": articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "app_home/article_detail.html", {"article": article})

from django.shortcuts import render, redirect
from .forms import CheckoutForm

def checkout(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            if payment_method == 'bank':
                return redirect('payment_qr')  # Link đến trang mã QR
            else:
                return redirect('order_success')  # Link đến trang xác nhận đơn hàng
    else:
        form = CheckoutForm()
    
    return render(request, 'milk_shop/checkout.html', {'form': form})


