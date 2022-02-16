from django.urls import path

from django_bootstrap_app import views

app_name = "django_bootstrap_app"

urlpatterns = [
    path("", views.index, name="index"),
]
