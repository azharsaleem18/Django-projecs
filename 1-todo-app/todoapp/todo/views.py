from django.db import models
from django.shortcuts import render
from .models import Todo
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TodoForm


class TodoView(TemplateView):
    template_name = 'todo_view.html'
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'objects_list': self.model.objects.all(),
        }
        return context

class TodoCreateView(CreateView):
    template_name = "create_todo.html"
    form_class = TodoForm
    success_url = reverse_lazy('todos')


class TodoUpdateView(UpdateView):
    template_name = "create_todo.html"
    form_class = TodoForm
    model = Todo
    success_url = reverse_lazy('todos')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)