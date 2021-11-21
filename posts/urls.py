from django.urls import path
from rest_framework.routers import SimpleRouter


# from .views import ListTodo, DetailTodo, UserDetail, UserList
from . views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', DetailTodo.as_view()),
#     path('', ListTodo.as_view()),
# ]

urlpatterns = router.urls