from django.urls import path
from .views import my_login, profile, my_logout, my_register


urlpatterns = [
    path("login/", my_login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", my_logout, name="logout"),
    path("register/", my_register, name="register"),
]
