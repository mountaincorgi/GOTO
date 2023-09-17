from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from Users.views import (
    HomeView, UserHomeView, UserLoginView, UserRegistrationView
)
 

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Main site
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("<username>/", UserHomeView.as_view(), name="user-home"),

    # REST framework testing
    path("api-auth", include("rest_framework.urls")),
]
