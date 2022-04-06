from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Income(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    comment = models.CharField(max_length=100)
    recurring_income = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #income_category = models.ForeignKey(IncomeCategory, null=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'

    def __str__(self):
        return self.name
