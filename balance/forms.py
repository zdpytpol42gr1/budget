from datetime import date

from django import forms
from django.core.validators import MaxValueValidator

from .models import Income, IncomeCategory, Expense, ExpenseCategory


class ExpenseForm(forms.ModelForm):
    expense_name = forms.CharField(error_messages={"required": "You must name the expense"}, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    expense_value = forms.DecimalField(error_messages={"required": "You must provide the value of the expense"}, label="Value", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label="Comment", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    expense_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', "placeholder": "YYYY-MM-DD"}), required=False, validators=[MaxValueValidator(date.today())])
    category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all(), error_messages={"required": "You must choose a category"}, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Expense
        fields = ["expense_name", "expense_value", "comment", "expense_date", "category"]


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["income_name", "income_value", "comment"]


class ExpenseCategoryForm(forms.ModelForm):
    expense_category_name = forms.CharField(label="Category name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = ExpenseCategory
        fields = ["expense_category_name"]


class IncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ["income_category_name"]
