from django import forms

from .models import Income, IncomeCategory


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["income_name", "income_value", "comment", "recurring_income"]


class IncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ["income_category_name"]
