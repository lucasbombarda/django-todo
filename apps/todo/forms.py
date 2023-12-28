from django import forms

from apps.todo.models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("completed", "task", "details")

        widgets = {
            "completed": forms.CheckboxInput(attrs={
                "class": "toggle toggle-success",
                "type": "checkbox",
            }),

            "task": forms.TextInput(attrs={
                "class": "input input-bordered",
                "type": "text",
                "placeholder": "Type your task...",
            }),

            "details": forms.Textarea(attrs={
                "class": "textarea textarea-bordered",
                "placeholder": "Type more details about your task...",
            })
        }
