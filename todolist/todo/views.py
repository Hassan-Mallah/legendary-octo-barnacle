from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


# Create your views here.
def index(request: HttpResponse):
    todos = Todo.objects.all()
    if request.method == 'POST':
        # for new task, save it to DB
        new_todo = Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')  # back to home page

    return render(request, 'index.html', context={'todos': todos})


# delete a task using pk
def delete(request: HttpResponse, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

