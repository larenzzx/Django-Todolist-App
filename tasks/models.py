from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # The user who owns this task (one user can have many tasks)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    # Task title (required, max 200 characters)
    title = models.CharField(max_length=200)

    # Task description (optional, can be blank)
    description = models.TextField(blank=True, null=True)

    # Is the task completed? Default is False (not completed)
    completed = models.BooleanField(default=False)

    # Automatically set when task is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updated when task is modified
    updated_at = models.DateTimeField(auto_now=True)

    # String representation (what shows up when you print a Task)
    def __str__(self):
        return self.title

    # Meta options for the model
    class Meta:
        # Order tasks by creation date (newest first)
        ordering = ['-created_at']
