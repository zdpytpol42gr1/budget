from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .filters import ExpenseFilter
from .mixins import AccessUserMixin
from .models import Expense, ExpenseCategory


class ExpenseListView(ListView):
    model = Expense

    def get_queryset(self):
        if self.model is not None:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)

            all_expenses_value = Expense.objects.aggregate(sum=Sum('expense_value'))
            context['all_expenses_value'] = round(all_expenses_value['sum'], 2)

            all_expenses_count = Expense.objects.count()
            context['all_expenses_count'] = all_expenses_count

            main_filter = ExpenseFilter(self.request.GET, queryset=Expense.objects.all())
            context['filter'] = main_filter

            results_count = main_filter.qs.count()
            context['results_count'] = results_count

            results_value = main_filter.qs.aggregate(sum=Sum('expense_value'))
            context['results_value'] = round(results_value['sum'], 2)

            return context

        except TypeError:
            pass


class ExpenseDetailView(AccessUserMixin, DetailView):
    model = Expense

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ['expense_name', 'expense_value', 'comment', 'recurring_expense', 'expense_date', 'expense_category']
    success_url = reverse_lazy('expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ['expense_name', 'expense_value', 'comment', 'recurring_expense', 'expense_date', 'expense_category']
    success_url = reverse_lazy('expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')

    def get_queryset(self):
        qs = super(ExpenseDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class ExpenseCategoryListView(ListView):
    model = ExpenseCategory
    template_name = 'balance/expense_category_list.html'


class ExpenseCategoryDetailView(DetailView):
    model = ExpenseCategory
    fields = '__all__'


class ExpenseCategoryCreateView(CreateView):
    model = ExpenseCategory
    fields = ['expense_category_name']
    template_name = 'balance/expense_category_form.html'
    success_url = reverse_lazy('expense_category_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCategoryDeleteView(DeleteView):
    model = ExpenseCategory
    fields = '__all__'
    template_name = 'balance/expense_category_confirm_delete.html'
    success_url = reverse_lazy('expense_category_list')

    def get_queryset(self):
        qs = super(ExpenseCategoryDeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


class ExpenseSummaryTemplateView(TemplateView):
    template_name = 'balance/expense_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = Expense.objects.all()
        context['expenses'] = expenses
        categories = ExpenseCategory.objects.all()
        context['categories'] = categories

        category_expenses_value = ExpenseCategory.objects.filter(
            expenses__expense_name="Shoes").aggregate(sum=Sum('expenses__expense_value'))
        context['category_expenses_value'] = round(category_expenses_value['sum'], 2)

        category_expenses_value2 = ExpenseCategory.objects.aggregate(sum=Sum('expenses__expense_value'))
        context['category_expenses_value2'] = round(category_expenses_value2['sum'], 2)

        for element in ExpenseCategory.objects.all():
            expenses_value_in_category = ExpenseCategory.objects.filter(expenses__expense_category=element.id).values_list("expenses__expense_value", flat=True)
            context["expenses_value"] = sum(expenses_value_in_category)

        return context
