from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

import django_filters
from .mixins import AccessUserMixin
from .models import Income, IncomeCategory


class IncomeListView(ListView):
    model = Income

    def get_queryset(self):
        if self.model is not None:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)

            all_incomes_value = Income.objects.aggregate(sum=Sum("income_value"))
            context["all_incomes_value"] = round(all_incomes_value["sum"], 2)

            all_incomes_count = Income.objects.count()
            context["all_incomes_count"] = all_incomes_count

            main_filter = IncomeFilter(self.request.GET, queryset=Income.objects.all())
            context["filter"] = main_filter

            results_count = main_filter.qs.count()
            context["results_count"] = results_count

            results_value = main_filter.qs.aggregate(sum=Sum("income_value"))
            context["results_value"] = round(results_value["sum"], 2)

            return context

        except TypeError:
            pass


class IncomeDetailView(AccessUserMixin, DetailView):
    model = Income

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class IncomeCreateView(CreateView):
    model = Income
    fields = "__all__"
    success_url = reverse_lazy("income_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(UpdateView):
    model = Income
    fields = "__all__"
    success_url = reverse_lazy("income_list")


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy("income_list")


class IncomeCategoryListView(ListView):
    model = IncomeCategory
    template_name = "balance/income_category_list.html"


class IncomeCategoryDetailView(DetailView):
    model = IncomeCategory
    fields = "__all__"


class IncomeCategoryCreateView(CreateView):
    model = IncomeCategory
    fields = "__all__"
    template_name = "balance/income_category_form.html"
    success_url = reverse_lazy("income_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryDeleteView(DeleteView):
    model = IncomeCategory
    fields = "__all__"
    template_name = "balance/income_category_confirm_delete.html"
    success_url = reverse_lazy("income_category_list")
