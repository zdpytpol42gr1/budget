from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class IncomeCategory(models.Model):
    income_category_name = models.CharField(max_length=50, unique=True)
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("id",)
        verbose_name = "Income Category"
        verbose_name_plural = "Income Categories"

    def __str__(self):
        return self.income_category_name


class Income(models.Model):
    name = models.CharField(max_length=30)
    income_value = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    comment = models.CharField(max_length=100, blank=True)
    recurring_income = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    income_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    income_category = models.ForeignKey(
        IncomeCategory, null=True, on_delete=models.SET_NULL
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-income_date",)
        verbose_name = "Income"
        verbose_name_plural = "Incomes"

    def __str__(self):
        return self.name
