from django. shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def toggle_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    todo.delete()
    return redirect('todo_list')