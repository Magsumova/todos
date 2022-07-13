from multiprocessing import context
from typing import Any
import django

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import QuerySet
from django.template import loader

from django.core.handlers.wsgi import WSGIRequest

from todo.models import (
    Task
    )
from todo.forms import (
    TaskForm
)

def index(
    request: WSGIRequest,
    *args,
    **kwargs
) -> HttpResponse:
    template_name = 'todo/main.html'
    return render(
        request,
        template_name,
    )

def create(
    request: WSGIRequest,
) -> HttpResponse:
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Не корректно введены данные'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(
        request,
        'todo/created.html',
        context
    )


def tasks(
    request: WSGIRequest,
    *args: tuple,
    **kwargs: dict
) -> HttpResponse:
    tasks: QuerySet = Task.objects.all()
    context = {
        'tasks': tasks
    }
    template_name = 'todo/tasks.html'
    return render(
        request,
        template_name,
        context
    )