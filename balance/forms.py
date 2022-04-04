from django import forms

from .models import Expense, ExpenseCategory


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name', 'expense_value', 'comment', 'recurring_expense']


class ExpenseCategory(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['expense_category_name']
