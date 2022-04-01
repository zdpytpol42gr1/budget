from django import forms
from django.apps import apps
from django.core.exceptions import ValidationError
from .models import IncomeCategory


def is_category_title_unique(income_category_title):
    if apps.get_model('balance.category').objects.filter(title=income_category_title).exists():
        raise ValidationError("This category already exists!")


class IncomeCategoryForm(forms.Form):
    required_css_class = "required"
    title = forms.CharField(label="Category title", validators=[is_category_title_unique, ])


class IncomeForm(forms.Form):
    name = forms.CharField(max_length=30)
    value = forms.DecimalField(decimal_places=2)
    recurring_income = forms.BooleanField()
    category = forms.ModelChoiceField(IncomeCategory.objects.all(), required=False)
