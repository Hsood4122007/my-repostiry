"""
Expense Tracker Admin Configuration
==================================
This module configures the Django admin interface for the expense tracking application.
It customizes how expenses are displayed and managed in the admin panel.

Admin Features:
- List display: Shows key expense information in the list view
- Filtering: Allows filtering by category and date
- Search: Enables searching by title and description
"""

from django.contrib import admin
from .models import Expense

# Register the Expense model with the admin interface
# This makes the Expense model visible and manageable in Django's admin panel
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Expense Admin Configuration
    --------------------------
    Customizes the admin interface for the Expense model.
    
    Configuration options:
    - list_display: Fields to display in the list view
    - list_filter: Fields to use for filtering
    - search_fields: Fields to include in search functionality
    """
    
    # Fields to display in the admin list view
    list_display = ['title', 'amount', 'category', 'date']
    
    # Fields to use for filtering in the admin interface
    list_filter = ['category', 'date']
    
    # Fields to include in the admin search functionality
    search_fields = ['title', 'description']
