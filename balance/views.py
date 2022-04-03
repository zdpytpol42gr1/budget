from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    fields = '__all__'
    success_url = reverse_lazy('expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = '__all__'
    success_url = reverse_lazy('expense_list')


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')


class ExpenseCategoryListView(ListView):
    model = ExpenseCategory
    template_name = 'balance/expense_category_list.html'


class ExpenseCategoryDetailView(DetailView):
    model = ExpenseCategory
    fields = '__all__'


class ExpenseCategoryCreateView(CreateView):
    model = ExpenseCategory
    fields = '__all__'
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
