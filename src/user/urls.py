from django.urls import path, include

from user.views import profile, login_view

app_name = "user"

urlpatterns = [
    path("profile", profile, name="profile"),
    path("login", login_view, name="login"),
]