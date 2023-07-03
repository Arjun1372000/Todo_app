from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewTaskForm, UpdateTaskForm
from .models import Task

# views contains functions which points towards the corresponding html files and passes required parameters to it.


def view_task(request):

    # filters the data inorder to only pass the incomplete tasks created by the current user
    tasks = Task.objects.filter(created_by=request.user, is_completed=False)

    return render(request, 'task/main.html', {
        'tasks': tasks,
    })


def completed_task(request):

    # filters the data inorder to only pass the completed tasks created by the current user
    tasks = Task.objects.filter(created_by=request.user, is_completed=True)

    return render(request, 'task/main_completed.html', {
        'tasks': tasks
    })


# decorator redirects to login page if the user is not authenticated
@login_required
def create(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()

            return redirect('/api/todo/view/')
    else:
        form = NewTaskForm()

    return render(request, 'task/form.html', {
        'form': form,
        'title': 'Create task'
    })


# decorator redirects to login page if the user is not authenticated
@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.delete()

    return redirect('task:completed')


# decorator redirects to login page if the user is not authenticated
@login_required
def update(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            form.save()

            return redirect('/api/todo/view/')
    else:
        form = UpdateTaskForm(instance=task)

    return render(request, 'task/form.html', {
        'form': form,
        'title': 'Update task'
    })
