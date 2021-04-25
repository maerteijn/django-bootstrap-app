from django.urls import path

from . import views

app_name = "django_bootstrap_app"

urlpatterns = [
    path("", views.index, name="index"),
]
