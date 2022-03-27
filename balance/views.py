from django.shortcuts import render
from .forms import IncomeForm


def balance_view(request):
    form = IncomeForm(request.POST)

    # if form.is_valid():
    #     form.save()
    return render(request, 'balance/panel.html', {'form': form})


def incomes_view(request, id):
    pass


def expenses_view(request, id):
    pass
