from django.urls import path, include

from core.views import ToDoListView, index, PersonView, MyListView

from core.api.views import ToDoViewSet, PersonViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', ToDoViewSet)
router.register('users', PersonViewSet)


urlpatterns = [
    path('mylist/', MyListView.as_view()),
    path('persons/', PersonView.as_view()),
    path('index/', index),
    path('todos/', ToDoListView.as_view()),
    path('api/', include(router.urls)),
]
