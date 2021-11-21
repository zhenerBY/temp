from rest_framework import serializers

from core.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
            'creator',
            'maker',
        ]