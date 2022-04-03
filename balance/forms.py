from django import forms

from .models import IncomeCategory, Income


class IncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ["title", "comment"]


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["name", "income_value", "comment", "recurring_income"]
