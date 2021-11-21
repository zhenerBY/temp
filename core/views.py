import random
from rest_framework import viewsets

from django.http import HttpResponse
from django.views.generic import ListView

from core.models import ToDo, Person
from core.serializers import ToDoSerializer



def index(request):
    return HttpResponse('<h1>HELLO WORLD!</h1>')


class ToDoListView(ListView):
    model = ToDo
    template_name = "todo_list.html"
    extra_context = {"name": "Vlad"}

    def get_context_data(self, **kwargs):
        context = {
            'object_list': self.object_list,
            'random_number': random.randint(10, 110)
        }
        return super().get_context_data(**context)

class PersonView(ListView):
    model = Person
    template_name = "persons_list.html"


class MyListView(ListView):
    model = ToDo
    template_name = 'my_todos.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(maker=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = {
            "current_user":self.request.user,
            'object_list': self.object_list,
        }
        return super().get_context_data(**context)

