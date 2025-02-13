from django.http import HttpResponse

def milkshop(request):
    return HttpResponse("<h1>Welcome to My Milk Shop!</h1>")
