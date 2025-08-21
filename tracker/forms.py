"""
Expense Tracker Forms
====================
This module defines the forms used for user input validation and data handling
in the expense tracking application. It uses Django's ModelForm to create
forms that automatically map to the Expense model.

The forms handle:
- User input validation
- Data sanitization
- HTML widget configuration for better user experience
"""

from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    """
    Expense Form
    ------------
    A ModelForm that automatically creates form fields based on the Expense model.
    
    This form handles:
    - Validation of expense data (amount must be positive, required fields)
    - Custom widget configuration for better user experience
    - Automatic saving of form data to the database
    
    Attributes:
        Meta: Inner class that defines the model and field configurations
    """
    
    class Meta:
        """
        Meta Configuration
        -----------------
        Defines how the form should behave and which fields to include.
        
        Attributes:
            model: The Django model this form is based on (Expense)
            fields: List of model fields to include in the form
            widgets: Custom HTML widgets for enhanced user experience
        """
        
        # Link this form to the Expense model
        model = Expense
        
        # Include all fields from the Expense model in the form
        fields = ['title', 'amount', 'category', 'date', 'description']
        
        # Custom widgets for better user experience
        widgets = {
            # Date picker widget for easy date selection
            'date': forms.DateInput(attrs={'type': 'date'}),
            
            # Textarea widget for description with 3 rows for better visibility
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_amount(self):
        """
        Custom validation for the amount field.
        Ensures the amount is a positive number.
        
        Returns:
            Decimal: The cleaned amount value
            
        Raises:
            forms.ValidationError: If amount is negative or zero
        """
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount
