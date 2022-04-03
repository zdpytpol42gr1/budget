from django.contrib.auth.models import User
from django.db import models


class Income(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.CharField(max_length=100)
    cyclical_income = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
