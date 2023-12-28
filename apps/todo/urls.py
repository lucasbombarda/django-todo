from django.urls import path

from apps.todo import views

app_name = "todo"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
]
