from django.urls import path, include
from .views import login_view, log_out, signup_view

app_name = "user"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", signup_view, name="signup"),
]
