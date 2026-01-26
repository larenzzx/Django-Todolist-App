from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task


@login_required
def task_list(request):
    """
    Display all tasks for the logged-in user.
    Only shows tasks that belong to the current user.
    """
    # Get all tasks for the current user, ordered by creation date (newest first)
    tasks = Task.objects.filter(user=request.user)

    # Count completed and pending tasks
    completed_count = tasks.filter(completed=True).count()
    pending_count = tasks.filter(completed=False).count()

    context = {
        'tasks': tasks,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    """
    Create a new task.
    GET: Show the create form
    POST: Save the new task
    """
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Validate that title is not empty
        if title:
            # Create the task
            Task.objects.create(
                user=request.user,
                title=title,
                description=description
            )
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:task_list')
        else:
            messages.error(request, 'Title is required!')

    return render(request, 'tasks/task_form.html', {'action': 'Create'})


@login_required
def task_update(request, pk):
    """
    Update an existing task.
    pk = primary key (task ID)
    """
    # Get the task or return 404 if not found or doesn't belong to user
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            task.title = title
            task.description = description
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks:task_list')
        else:
            messages.error(request, 'Title is required!')

    context = {
        'task': task,
        'action': 'Update'
    }
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_delete(request, pk):
    """
    Delete a task.
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('tasks:task_list')

    context = {'task': task}
    return render(request, 'tasks/task_confirm_delete.html', context)


@login_required
def task_toggle(request, pk):
    """
    Toggle task completion status (completed ↔ not completed).
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)

    # Toggle the completed status
    task.completed = not task.completed
    task.save()

    # Success message
    status = 'completed' if task.completed else 'marked as pending'
    messages.success(request, f'Task "{task.title}" {status}!')

    return redirect('tasks:task_list')
