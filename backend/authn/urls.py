from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("api/register", views.UserRegistrationView.as_view(), name="register"),
    path("api/login", views.UserLoginView.as_view(), name="login"),
]
