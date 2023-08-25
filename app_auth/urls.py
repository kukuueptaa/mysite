from django.urls import path
from .views import my_login


urlpatterns = [
    path("login/", my_login, name="login"),
]
