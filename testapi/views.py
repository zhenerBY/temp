from django.shortcuts import render

from rest_framework import generics, permissions

from core.models import ToDo
from .serializers import ToDoSerializer
from .permissions import IsAuthorOrReadOnly


class ListTodo(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DetailTodo(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer