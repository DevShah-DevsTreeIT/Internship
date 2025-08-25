from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# View to list all expenses
def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

# View to add a new expense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})



# def login_view(request):
#     if request.method == 'POST':
#         # form receives user input
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             # cleaned data after validation
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             # check user credentials
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('expense_list')  # or wherever you want to go after login
#         # if not valid, show form with errors
#     else:
#         form = AuthenticationForm()  # blank form for GET request

#     return render(request, 'expenses/login.html', {'form': form})




# def logout_view(request):
#     # if request.method == 'POST':
#         # form receives user input
#     pass