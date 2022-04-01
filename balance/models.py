from django.db import models


class IncomeCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('id', )
        verbose_name = 'Income Category'
        verbose_name_plural = 'Income Categories'

    def __str__(self):
        return self.title


class Income(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    recurring_income = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    income_category = models.ForeignKey(IncomeCategory, null=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ('id', )
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'

    def __str__(self):
        return self.name
