from django import forms
from django.forms import ModelForm
from . import models


# class IncomeForm(forms.ModelForm):
#     class Meta:
#         model = models.Income
#         fields = '__all__'

class IncomeForm(forms.Form):
    name = forms.CharField(max_length=30, label='income name', required=True)
    category = forms.CharField(max_length=30, label='category name', required=True)
    value = forms.DecimalField(min_value=1, required=True, max_digits=6)
    comment = forms.CharField(max_length=100)
    cyclical_income = forms.ChoiceField(choices=(('1', 'Yes'), ('0', 'No')), required=True)  # extra