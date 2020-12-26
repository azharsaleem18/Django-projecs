from django.db import models
from django.shortcuts import render
from .models import Todo
from django.views.generic import TemplateView


class TodoView(TemplateView):
    template_name = 'todo_view.html'
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'objects_list': self.model.objects.all(),
        }
        return context