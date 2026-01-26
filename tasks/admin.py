from django.contrib import admin
from .models import Task

# Register your models here.

# this is the simple version. no filtering just display the model
# admin.site.register(Task)

# this way is to customize the look on the admin portal. it will include filterings
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('title', 'user', 'completed', 'created_at', 'updated_at')

    # Add filters in the sidebar
    list_filter = ('completed', 'created_at', 'user')

    # Add search functionality
    search_fields = ('title', 'description')

    # Make certain fields clickable to edit
    list_editable = ('completed',)

    # Order by creation date (newest first)
    ordering = ('-created_at',)
