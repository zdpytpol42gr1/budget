from decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from .filters import ExpenseFilter, IncomeFilter
from .forms import ExpenseForm, ExpenseCategoryForm
from .mixins import AccessUserMixin
from .models import Expense, ExpenseCategory, Income, IncomeCategory


class IncomeListView(ListView):
    model = Income

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_incomes_value = Income.objects.aggregate(sum=Sum("income_value"))
        context["all_incomes_value"] = all_incomes_value["sum"]

        all_incomes_count = Income.objects.count()
        context["all_incomes_count"] = all_incomes_count

        main_filter = IncomeFilter(self.request.GET, queryset=Income.objects.all())
        context['filter'] = main_filter

        results_count = main_filter.qs.count()
        context['results_count'] = results_count

        results_value = main_filter.qs.aggregate(sum=Sum('income_value'))
        context['results_value'] = results_value['sum']

        return context


class ExpenseListView(ListView):
    model = Expense

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_expenses_value = Expense.objects.aggregate(sum=Sum("expense_value"))
        context["all_expenses_value"] = all_expenses_value["sum"]

        all_expenses_count = Expense.objects.count()
        context["all_expenses_count"] = all_expenses_count

        main_filter = ExpenseFilter(self.request.GET, queryset=Expense.objects.all())
        context["filter"] = main_filter

        results_count = main_filter.qs.count()
        context["results_count"] = results_count

        results_value = main_filter.qs.aggregate(sum=Sum("expense_value"))
        context["results_value"] = results_value["sum"]

        return context


class IncomeDetailView(AccessUserMixin, DetailView):
    model = Income

    def test_func(self):
        obj = self.get_object()
        return obj.user, self.request.user


class ExpenseDetailView(AccessUserMixin, DetailView):
    model = Expense

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class IncomeCreateView(CreateView):
    model = Income
    fields = [
        "income_name",
        "income_value",
        "comment",
        "recurring_income",
        "income_date",
        "income_category",
    ]
    success_url = reverse_lazy("income_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm

    success_url = reverse_lazy("expense_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = "balance/expense_update_form.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("expense_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(UpdateView):
    model = Income
    template_name = "balance/income_update_form.html"
    fields = [
        "income_name",
        "income_value",
        "comment",
        "recurring_income",
        "income_date",
        "income_category",
    ]
    success_url = reverse_lazy("income_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy("income_list")

    def get_queryset(self):
        qs = super(IncomeDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class IncomeCategoryListView(ListView):
    model = IncomeCategory
    template_name = "balance/income_category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = IncomeCategory.objects.all()
        context['categories'] = categories

        sum_of_incomes_in_category = IncomeCategory.objects.annotate(
            sum=Sum("income__income_value")
        )
        context["sum_of_incomes_in_category"] = sum_of_incomes_in_category
        return context


class IncomeCategoryDetailView(DetailView):
    model = IncomeCategory
    template_name = "balance/income_category_detail.html"


class IncomeCategoryCreateView(CreateView):
    model = IncomeCategory
    fields = ["income_category_name"]
    template_name = "balance/income_category_form.html"
    success_url = reverse_lazy("income_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy("expense_list")

    def get_queryset(self):
        qs = super(ExpenseDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class ExpenseCategoryListView(ListView):
    model = ExpenseCategory
    template_name = "balance/expense_category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = ExpenseCategory.objects.all()
        context['categories'] = categories

        sum_of_expenses_in_category = ExpenseCategory.objects.annotate(
            sum=Sum("expense__expense_value")
        )
        context["sum_of_expenses_in_category"] = sum_of_expenses_in_category
        return context


class ExpenseCategoryDetailView(DetailView):
    model = ExpenseCategory
    template_name = "balance/expense_category_detail.html"


class ExpenseCategoryCreateView(CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm

    template_name = "balance/expense_category_form.html"
    success_url = reverse_lazy("expense_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCategoryUpdateView(UpdateView):
    model = ExpenseCategory
    fields = ["expense_category_name"]
    template_name = "balance/expense_category_update_form.html"
    success_url = reverse_lazy("expense_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryUpdateView(UpdateView):
    model = IncomeCategory
    fields = ["income_category_name"]
    template_name = "balance/income_category_update_form.html"
    success_url = reverse_lazy("income_category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryDeleteView(DeleteView):
    model = IncomeCategory
    template_name = "balance/income_category_confirm_delete.html"
    success_url = reverse_lazy("income_category_list")

    def get_queryset(self):
        qs = super(IncomeCategoryDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class ExpenseCategoryDeleteView(DeleteView):
    model = ExpenseCategory
    template_name = "balance/expense_category_confirm_delete.html"
    success_url = reverse_lazy("expense_category_list")

    def get_queryset(self):
        qs = super(ExpenseCategoryDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class DashboardTemplateView(TemplateView):
    model = Expense, Income
    template_name = 'balance/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        expenses = Expense.objects.all()
        context["expenses"] = expenses

        categories = ExpenseCategory.objects.all()
        context["categories"] = categories

        all_expenses_value = Expense.objects.aggregate(sum=Sum("expense_value"))
        context["all_expenses_value"] = all_expenses_value["sum"]

        all_incomes_value = Income.objects.aggregate(sum=Sum("income_value"))
        context["all_incomes_value"] = all_incomes_value["sum"]

        sum_of_expenses_in_category = ExpenseCategory.objects.annotate(
            Sum("expense__expense_value"))
        context["sum_of_expenses_in_category"] = sum_of_expenses_in_category

        sum_of_incomes_in_category = IncomeCategory.objects.annotate(Sum("income__income_value"))
        context["sum_of_incomes_in_category"] = sum_of_incomes_in_category

        january_expenses = Expense.objects.filter(expense_date__month=1).aggregate(sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["january_expenses"] = january_expenses["sum"]
        february_expenses = Expense.objects.filter(expense_date__month=2).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["february_expenses"] = february_expenses["sum"]
        march_expenses = Expense.objects.filter(expense_date__month=3).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["march_expenses"] = march_expenses["sum"]
        april_expenses = Expense.objects.filter(expense_date__month=4).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["april_expenses"] = april_expenses["sum"]
        may_expenses = Expense.objects.filter(expense_date__month=5).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0.0"))))
        context["may_expenses"] = may_expenses["sum"]
        june_expenses = Expense.objects.filter(expense_date__month=6).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["june_expenses"] = june_expenses["sum"]
        july_expenses = Expense.objects.filter(expense_date__month=7).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["july_expenses"] = july_expenses["sum"]
        august_expenses = Expense.objects.filter(expense_date__month=8).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["august_expenses"] = august_expenses["sum"]
        september_expenses = Expense.objects.filter(expense_date__month=9).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["september_expenses"] = september_expenses["sum"]
        october_expenses = Expense.objects.filter(expense_date__month=10).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["october_expenses"] = october_expenses["sum"]
        november_expenses = Expense.objects.filter(expense_date__month=11).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["november_expenses"] = november_expenses["sum"]
        december_expenses = Expense.objects.filter(expense_date__month=12).aggregate(
            sum=(Coalesce(Sum("expense_value"), Decimal("0"))))
        context["december_expenses"] = december_expenses["sum"]

        january_incomes = Income.objects.filter(income_date__month=1).aggregate(sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["january_incomes"] = january_incomes["sum"]
        february_incomes = Income.objects.filter(income_date__month=2).aggregate(sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["february_incomes"] = february_incomes["sum"]
        march_incomes = Income.objects.filter(income_date__month=3).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["march_incomes"] = march_incomes["sum"]
        april_incomes = Income.objects.filter(income_date__month=4).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["april_incomes"] = april_incomes["sum"]
        may_incomes = Income.objects.filter(income_date__month=5).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0.0"))))
        context["may_incomes"] = may_incomes["sum"]
        june_incomes = Income.objects.filter(income_date__month=6).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["june_incomes"] = june_incomes["sum"]
        july_incomes = Income.objects.filter(income_date__month=7).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["july_incomes"] = july_incomes["sum"]
        august_incomes = Income.objects.filter(income_date__month=8).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["august_incomes"] = august_incomes["sum"]
        september_incomes = Income.objects.filter(income_date__month=9).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["september_incomes"] = september_incomes["sum"]
        october_incomes = Income.objects.filter(income_date__month=10).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["october_incomes"] = october_incomes["sum"]
        november_incomes = Income.objects.filter(income_date__month=11).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["november_incomes"] = november_incomes["sum"]
        december_incomes = Income.objects.filter(income_date__month=12).aggregate(
            sum=(Coalesce(Sum("income_value"), Decimal("0"))))
        context["december_incomes"] = december_incomes["sum"]

        return context
