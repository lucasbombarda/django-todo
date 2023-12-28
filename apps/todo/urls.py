from django.urls import path

from apps.todo import views

app_name = "todo"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("new/", views.NewTodo.as_view(), name="new-todo"),
    path("edit/<int:pk>/", views.EditTodo.as_view(), name="edit-todo"),
    path("delete/<int:pk>/", views.DeleteTodo.as_view(), name="delete-todo"),
]
