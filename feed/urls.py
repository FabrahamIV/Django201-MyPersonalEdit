from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    # path("login/", auth_views.LoginView.as_view(), name="login")
]