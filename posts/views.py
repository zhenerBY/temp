from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Post
from .serializers import ToDoSerializer
from .permissions import IsAuthorOrReadOnly


class ListTodo(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = ToDoSerializer


class DetailTodo(generics.RetrieveAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = ToDoSerializer