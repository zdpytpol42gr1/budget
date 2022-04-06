import django_filters

from .models import IncomeCategory


class IncomeFilter(django_filters.FilterSet):
    income_value = django_filters.NumberFilter(
        field_name="income_value", label="exact value"
    )
    income_value__gte = django_filters.NumberFilter(
        field_name="income_value", lookup_expr="gte", label="from"
    )
    income_value__lte = django_filters.NumberFilter(
        field_name="income_value", lookup_expr="lte", label="to"
    )
    income_name = django_filters.CharFilter(
        lookup_expr="icontains", label="income_name"
    )
    income_category = django_filters.ModelChoiceFilter(
        queryset=IncomeCategory.objects.all(), label="income_category"
    )
