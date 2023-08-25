from django.shortcuts import render


def my_login(request):
    return render(request, 'app_auth/login.html')
