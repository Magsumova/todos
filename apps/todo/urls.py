from os import path
from django.urls import (
    path
)

from todo.views import (
    index,
    create,
    tasks
)

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('tasks/', tasks, name='tasks'),
]