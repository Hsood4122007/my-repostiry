"""
Expense Tracker URL Configuration
=================================
This module defines the URL patterns (routes) for the expense tracking application.
It maps URLs to their corresponding view functions.

URL Patterns:
- '' (root): Maps to the expense list view
- 'add/': Maps to the add expense view
- 'delete/<int:expense_id>/': Maps to the delete expense view

These URLs are included in the main project's URL configuration.
"""

from django.urls import path
from . import views

# Define URL patterns for the tracker app
urlpatterns = [
    # Root URL - displays the list of all expenses
    # Example: http://localhost:8000/
    path('', views.expense_list, name='expense_list'),
    
    # Add expense URL - displays form to add new expense
    # Example: http://localhost:8000/add/
    path('add/', views.add_expense, name='add_expense'),
    
    # Delete expense URL - handles deletion of existing expense
    # Example: http://localhost:8000/delete/5/ (where 5 is the expense ID)
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
