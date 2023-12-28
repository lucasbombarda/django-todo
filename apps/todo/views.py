from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from apps.todo.forms import TodoForm
from apps.todo.models import Todo


class Home(ListView):
    template_name = "todo/pages/home.html"
    model = Todo
    context_object_name = "todos"


class NewTodo(CreateView):
    template_name = "todo/pages/new_todo.html"
    form_class = TodoForm
    success_url = reverse_lazy("todo:home")

    def form_valid(self, form):
        messages.success(self.request, "Todo added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "An error occurred.")
        return super().form_invalid(form)


class EditTodo(UpdateView):
    template_name = "todo/pages/edit_todo.html"
    form_class = TodoForm
    model = Todo
    success_url = reverse_lazy("todo:home")

    def form_valid(self, form):
        messages.success(self.request, "Todo edited successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "An error occurred.")
        return super().form_invalid(form)


class DeleteTodo(View):

    def post(self, request, pk, *args, **kwargs):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.delete()
            messages.success(self.request, "Todo removed successfully!")
        except Todo.DoesNotExist:
            messages.error(self.request, "Todo doesn't exists")

        return redirect("todo:home")
