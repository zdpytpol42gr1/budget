from django import forms
from django.forms import ModelForm
from . import models


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = "__all__"
