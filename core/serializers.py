from rest_framework import serializers, generics

from core.models import ToDo, User, Person


class ToDoSerializer(serializers.ModelSerializer):
    # random_number = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
            'creator',
            'maker',
            # 'random_number',
            'user_name',
        ]

    def get_user_name(self, object):
        return object.creator.first_name

    def get_random_number(self, object, *arg, **kwargs):
        print(object.creator.first_name)
        import random
        return random.randint(10, 100)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]


class ToDoDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    maker = UserSerializer()

    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
            'creator',
            'maker',
        ]


# class ToDoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToDo
#         fields =[
#             'id',
#             'name',
#             'description',
#             'creator',
#             'maker',
#         ]

class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
            'creator',
            'maker',
        ]


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]


class PresonDetailSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()
    # maker = UserSerializer()
    # created_todos = serializers.StringRelatedField(many=True)
    # created_todos = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='todo-detail'
    # )
    created_todos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    made_todos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='todo-detail'
    )

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'created_todos',
            'made_todos',
        ]
