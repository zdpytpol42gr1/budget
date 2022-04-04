from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    comment = models.TextField(blank=True)
    recurring_expense = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expense_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    expense_category = models.ForeignKey('balance.ExpenseCategory', null=True, on_delete=models.SET_NULL, related_name='expenses')

    class Meta:
        ordering = ("-expense_date",)

    def __str__(self):
        return self.expense_name


class ExpenseCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('expense_category_name',)
        verbose_name_plural = "Expense Categories"

    def __str__(self):
        return self.expense_category_name
