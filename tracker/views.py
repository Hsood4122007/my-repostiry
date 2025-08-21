"""
Expense Tracker Views
====================
This module contains the view functions that handle HTTP requests and responses
for the expense tracking application. Views act as the middle layer between
the models (data) and templates (presentation).

Available views:
- expense_list: Displays all expenses with total calculation
- add_expense: Handles both GET (display form) and POST (process form) requests
- delete_expense: Handles deletion of existing expenses
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    """
    Expense List View
    ----------------
    Displays a list of all expenses in chronological order (newest first).
    
    Functionality:
    - Retrieves all expense records from the database
    - Orders expenses by date (newest first)
    - Calculates the total amount of all expenses
    - Passes data to the template for rendering
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Rendered HTML page showing the expense list
    """
    
    # Retrieve all expenses from the database, ordered by date (newest first)
    expenses = Expense.objects.all().order_by('-date')
    
    # Calculate the total amount of all expenses using Python's sum function
    # This is done in-memory after fetching all records
    total = sum(expense.amount for expense in expenses)
    
    # Create context dictionary to pass data to the template
    context = {
        'expenses': expenses,  # List of all expense objects
        'total': total,        # Calculated total amount
    }
    
    # Render the expense_list.html template with the context data
    return render(request, 'tracker/expense_list.html', context)

def add_expense(request):
    """
    Add Expense View
    ----------------
    Handles both displaying the expense form and processing form submissions.
    
    GET Request: Displays a blank expense form
    POST Request: Processes the submitted form data
    
    Functionality:
    - Creates new ExpenseForm instance
    - Validates submitted data
    - Saves valid data to the database
    - Redirects to expense list on successful submission
    
    Args:
        request (HttpRequest): The HTTP request object
        
    Returns:
        HttpResponse: Either the form page (GET) or redirect to list (POST success)
    """
    
    # Check if this is a form submission (POST request)
    if request.method == 'POST':
        # Create form instance with submitted data
        form = ExpenseForm(request.POST)
        
        # Check if the submitted data is valid
        if form.is_valid():
            # Save the valid form data to the database
            form.save()
            
            # Show success message to user
            messages.success(request, 'Expense added successfully!')
            
            # Redirect to the expense list page after successful submission
            return redirect('expense_list')
    else:
        # For GET requests, create a blank form instance
        form = ExpenseForm()
    
    # Create context dictionary for the template
    context = {
        'form': form,  # Form instance (either blank or with errors)
    }
    
    # Render the add_expense.html template with the form
    return render(request, 'tracker/add_expense.html', context)

def delete_expense(request, expense_id):
    """
    Delete Expense View
    ------------------
    Handles the deletion of an existing expense.
    
    Security Features:
    - Uses get_object_or_404 to prevent deletion of non-existent expenses
    - Only accepts POST requests to prevent accidental deletions
    
    Functionality:
    - Retrieves the expense by ID
    - Deletes the expense from the database
    - Shows success message to user
    - Redirects back to expense list
    
    Args:
        request (HttpRequest): The HTTP request object
        expense_id (int): The primary key of the expense to delete
        
    Returns:
        HttpResponse: Redirect to expense list after deletion
    """
    
    # Only allow POST requests for security (prevents accidental deletions)
    if request.method == 'POST':
        # Get the expense object or return 404 if not found
        expense = get_object_or_404(Expense, id=expense_id)
        
        # Store expense details for the success message
        expense_title = expense.title
        expense_amount = expense.amount
        
        # Delete the expense from the database
        expense.delete()
        
        # Show success message to user
        messages.success(request, f'Expense "{expense_title}" (${expense_amount}) deleted successfully!')
    
    # Always redirect back to the expense list
    return redirect('expense_list')
