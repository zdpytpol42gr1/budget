from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)

from .mixins import AccessUserMixin
from .models import Income, IncomeCategory


class IncomeListView(ListView):
    model = Income
    template_name = "balance/income_list.html"

    def get_queryset(self):
        if self.model is not None:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incomes_value = Income.objects.filter(user=self.request.user).values_list(
            "income_value", flat=True
        )
        context["incomes_value"] = sum(incomes_value)
        incomes_counter = Income.objects.filter(user=self.request.user).count()
        context["incomes_counter"] = incomes_counter
        return context


class IncomeCreateView(CreateView):
    model = Income
    fields = ["name", "income_value", "comment", "recurring_income", "income_category"]
    template_name = "balance/income_form.html"
    success_url = reverse_lazy("income_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeDetailView(AccessUserMixin, DetailView):
    model = Income
    template_name = "balance/income_detail.html"


class IncomeUpdateView(AccessUserMixin, UpdateView):
    model = Income
    fields = ["name", "income_value", "comment", "recurring_income"]
    template_name = "balance/income_form.html"
    success_url = reverse_lazy("income_list")


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "balance/income_confirm_delete.html"
    success_url = reverse_lazy("income_list")

    def get_object(self, queryset=None):
        obj = super(IncomeDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Exception("That's not your Income!")
        return obj


class IncomeCategoryListView(ListView):
    model = IncomeCategory
    context_object_name = "income_category_list"
    queryset = IncomeCategory.objects.all()
    template_name = "balance/income_category_list.html"

    def get_queryset(self):
        if self.model is not None:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incomes_category_counter = IncomeCategory.objects.filter(
            user=self.request.user
        ).count()
        context["incomes_category_counter"] = incomes_category_counter
        return context


class IncomeCategoryCreateView(CreateView):
    model = IncomeCategory
    template_name = "balance/income_category_form.html"
    success_url = reverse_lazy("income_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryDetailView(AccessUserMixin, DetailView):
    model = IncomeCategory
    template_name = "balance/income_category_detail.html"


class IncomeCategoryUpdateView(AccessUserMixin, UpdateView):
    model = IncomeCategory
    fields = ["title", "comment"]
    template_name = "balance/income_category_form.html"
    success_url = reverse_lazy("income_category_list")


class IncomeCategoryDeleteView(DeleteView):
    model = IncomeCategory
    template_name = "balance/income_category_confirm_delete.html"
    success_url = reverse_lazy("income_category_list")

    def get_queryset(self):
        qs = super(IncomeCategoryDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)
