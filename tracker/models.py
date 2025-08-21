"""
Expense Tracker Models
======================
This module defines the database models for the expense tracking application.
It contains the Expense model which represents individual expense records.

The Expense model includes fields for:
- Basic expense information (title, amount, description)
- Categorization (category selection)
- Date tracking (when the expense occurred)
"""

from django.db import models
from django.utils import timezone

class Expense(models.Model):
    """
    Expense Model
    -----------
    Represents an individual expense record in the database.
    
    Attributes:
        title (CharField): Short description/name of the expense (max 100 chars)
        amount (DecimalField): The monetary value of the expense (max 10 digits, 2 decimal places)
        category (CharField): Category classification with predefined choices
        date (DateField): When the expense was incurred (defaults to current date)
        description (TextField): Optional detailed description of the expense
    """
    
    # Predefined expense categories for consistent classification
    CATEGORY_CHOICES = [
        ('food', 'Food'),                    # Food and dining expenses
        ('transport', 'Transport'),          # Transportation costs (fuel, public transport, etc.)
        ('shopping', 'Shopping'),           # Shopping expenses (clothes, electronics, etc.)
        ('utilities', 'Utilities'),         # Utility bills (electricity, water, internet, etc.)
        ('entertainment', 'Entertainment'),   # Entertainment expenses (movies, games, etc.)
        ('other', 'Other'),                 # Any other expenses not covered above
    ]
    
    # Core expense information
    title = models.CharField(max_length=100, help_text="Brief description of the expense")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Expense amount in dollars")
    
    # Categorization for expense analysis and reporting
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        help_text="Select the category that best describes this expense"
    )
    
    # Date tracking for chronological organization
    date = models.DateField(default=timezone.now, help_text="Date when the expense was incurred")
    
    # Optional detailed description for additional context
    description = models.TextField(blank=True, help_text="Optional detailed description of the expense")
    
    def __str__(self):
        """
        String representation of the expense.
        Returns a formatted string showing the expense title and amount.
        """
        return f"{self.title} - ${self.amount}"
    
    class Meta:
        """
        Meta options for the Expense model.
        """
        # Default ordering by date (newest first)
        ordering = ['-date']
        
        # Singular and plural names for admin interface
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
