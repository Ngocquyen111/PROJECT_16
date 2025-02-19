from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Họ và Tên")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=15, label="Số điện thoại")
    address = forms.CharField(widget=forms.Textarea, label="Địa chỉ")
    payment_method = forms.ChoiceField(
        choices=[('cod', 'Thanh toán khi nhận hàng'), ('bank', 'Chuyển khoản')],
        widget=forms.RadioSelect,
        label="Phương thức thanh toán"
    )