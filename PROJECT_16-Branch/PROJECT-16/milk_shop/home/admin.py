from django.contrib import admin
from .models import User, Product, Order, Voucher, BlogPost, Feedback

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Voucher)
admin.site.register(BlogPost)
admin.site.register(Feedback)

