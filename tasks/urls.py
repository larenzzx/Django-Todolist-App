from django.urls import path
from . import views

# App name for namespacing URLs (so we can use 'tasks:task_list' in templates)
app_name = 'tasks'

urlpatterns = [
    # Home page - list all tasks
    path('', views.task_list, name='task_list'),

    # Create new task
    path('create/', views.task_create, name='task_create'),

    # Update existing task (pk = primary key / task ID)
    path('update/<int:pk>/', views.task_update, name='task_update'),

    # Delete task
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),

    # Toggle task completion
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
]
