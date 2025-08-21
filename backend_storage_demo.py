# Simple Django Backend Storage Demo
# This shows how your expense tracker stores data in the backend

from django.db import models
from django.utils import timezone

# Your Expense model (already defined in models.py)
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=[
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ])
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

# Code to store data in backend:
# 1. Create new expense
new_expense = Expense(
    title="Coffee Shop",
    amount=5.50,
    category="food",
    description="Morning coffee at Starbucks"
)
new_expense.save()  # This stores data in SQLite database

# 2. Retrieve all expenses
all_expenses = Expense.objects.all()

# 3. Filter expenses
food_expenses = Expense.objects.filter(category='food')

# 4. Update expense
expense = Expense.objects.get(id=1)
expense.amount = 6.00
expense.save()

# 5. Delete expense
Expense.objects.get(id=1).delete()
