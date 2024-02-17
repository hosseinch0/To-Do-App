from django.urls import path, include
from .views import login_view, log_out, signup_view, profile, profile_edit

app_name = "user"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile, name="profile"),
    path("profile/edit/<int:pk>", profile_edit, name="edit")
]
