from django.db import models # Django's model system
from django.contrib.auth.models import User # Built-in User model

# Create your models here.

class Task(models.Model):
    # The user who owns this task (one user can have many tasks)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    # Links each task to a user
    # ForeignKey = "This task belongs to one user"
    # on_delete=models.CASCADE means: "If user is deleted, delete their tasks too"
    # related_name='tasks' lets you access user.tasks.all()
    

    # Task title (required, max 200 characters)
    title = models.CharField(max_length=200)
    # Short text field (required)
    # max_length=200 means maximun 200 characters

    # Task description (optional, can be blank)
    description = models.TextField(blank=True, null=True)
    # Long text field (optional)
    # blank=True means forms can leave it empty
    # null=True means database can store NULL
    

    # Is the task completed? Default is False (not completed)
    completed = models.BooleanField(default=False)
    # True/False field
    # default=False means new tasks start as incomplete

    # Automatically set when task is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updated when task is modified
    updated_at = models.DateTimeField(auto_now=True)

    # String representation (what shows up when you print a Task)
    def __str__(self):
        return self.title
    # When you print a Task object, it shows the title
    # Example: print(taks) -> "Buy groceries"

    # Meta options for the model
    class Meta:
        # Order tasks by creation date (newest first)
        ordering = ['-created_at']
    # Tasks are orderesd by creation date, newest first
    # The minus sign (-) means descending order
