from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ExpenseForm
from .models import *


# Create your views here.

def home(request):
    form = ExpenseForm()
    if request.method == 'POST':
        print(request.POST)
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            form = ExpenseForm()

    expenses = Expense.objects.all().order_by('-pk')
    total = sum(expenses.values_list('amount', flat=True))
    context = {'form': form, 'expenses': expenses, 'total': total}

    return render(request, 'index.html', context)


def dashboard(request):
    labels = []
    data = []
    count = {}
    expenses = Expense.objects.all().order_by('-pk')
    for expense in expenses:
        labels.append(expense.category.category_name)
        data.append(expense.amount)
        if expense.category.category_name not in count :
            count[expense.category.category_name] = expense.amount
        else:
            count[expense.category.category_name] += expense.amount

    labels = (list(count.keys()))
    data = (list(count.values()))
    print(labels)
    print(data)

    context = {'labels': labels, 'data': data}
    return render(request, 'dashboard.html', context)
