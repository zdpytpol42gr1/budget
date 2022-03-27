from django.db import models


# class Income(models.Model):
#     name = models.CharField(max_length=30, label='income name', required=True)
#     category = models.CharField(max_length=30, label='category name', required=True)
#     value = models.DecimalField(min_value=1, required=True, max_digits=6)
#     comment = models.CharField(max_length=100)
#     cyclical_income = models.ChoiceField(choices=(('1', 'Yes'), ('0', 'No')), required=True)  # extra