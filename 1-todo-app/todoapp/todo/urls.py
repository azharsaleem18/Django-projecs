from django.urls import path
from .views import TodoView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('todos/', TodoView.as_view(), name='todos'),
    path('todos/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delet'),
]