from django import forms


from .models import Income, IncomeCategory, Expense, ExpenseCategory


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["expense_name", "expense_value", "comment", "recurring_expense"]


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["income_name", "income_value", "comment", "recurring_income"]


class ExpenseCategory(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["expense_category_name"]


class IncomeCategory(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ["income_category_name"]
