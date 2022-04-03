import django_filters.filters

from .models import ExpenseCategory


class ExpenseFilter(django_filters.FilterSet):
    expense_value = django_filters.NumberFilter(field_name='expense_value', label='exact value')
    expense_value__gte = django_filters.NumberFilter(field_name='expense_value', lookup_expr='gte', label='from')
    expense_value__lte = django_filters.NumberFilter(field_name='expense_value', lookup_expr='lte', label='to')
    expense_name = django_filters.CharFilter(lookup_expr='icontains', label='name')
    expense_category = django_filters.ModelChoiceFilter(queryset=ExpenseCategory.objects.all(), label='category')
