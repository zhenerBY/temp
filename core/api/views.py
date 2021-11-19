from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import ToDo, Person
from core.serializers import ToDoSerializer, ToDoDetailSerializer, ToDoCreateSerializer, UserSerializer, \
    PersonCreateSerializer, PresonDetailSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ToDoDetailSerializer
        elif self.action == 'create':
            return ToDoCreateSerializer
        return ToDoSerializer

    @action(methods=['POST'], detail=True)
    def change_creator(self, *args, **kwargs):
        todo = self.get_object()
        creator_data = self.request.data.get('crator')
        if isinstance(creator_data, int):
            creator = Person.objects.get(pk=creator_data)
        else:
            creator_serializer = UserSerializer(data=creator_data)
            creator_serializer.is_valid(raise_exception=True)
            creator = creator_serializer.save()
        todo.creator = creator
        todo.save()
        return Response(ToDoDetailSerializer(todo).data, status=status.HTTP_201_CREATED)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PresonDetailSerializer
        if self.action == 'create':
            return PersonCreateSerializer
        return UserSerializer

    # @action(methods=['POST'], detail=True)
    # def change_creator(self, *args, **kwargs):
    #     todo = self.get_object()
    #     creator_data = self.request.data.get('crator')
    #     if isinstance(creator_data, int):
    #         creator = Person.objects.get(pk=creator_data)
    #     else:
    #         creator_serializer = UserSerializer(data=creator_data)
    #         creator_serializer.is_valid(raise_exception=True)
    #         creator = creator_serializer.save()
    #     todo.creator = creator
    #     todo.save()
    #     return Response(ToDoDetailSerializer(todo).data, status=status.HTTP_201_CREATED)
