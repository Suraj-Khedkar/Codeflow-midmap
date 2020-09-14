from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexs"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("Aboutus", views.aboutus ,name="about")
]