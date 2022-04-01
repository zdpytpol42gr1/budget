from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_value = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    cyclical_expense = models.BooleanField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expense_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    category = models.ForeignKey('balance.Category', on_delete=models.CASCADE, related_name="expenses")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.expense_name


class Category(models.Model):
    # value, human readable name
    CATEGORY_CHOICES = [
        ("Rent", "Rent"),
        ("Bills", "Bills"),
        ("3", "Groceries"),
        ("4", "Dining out"),
        ("5", "Transportation"),
        ("6", "Entertainment"),
        ("7", "Savings"),
        ("8", "Clothing"),
        ("9", "Beauty"),
        ("10", "Health"),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
