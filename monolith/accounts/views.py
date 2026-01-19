from django.shortcuts import render, redirect
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   # 👈 THIẾU DÒNG NÀY

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        customer = Customer.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).first()

        if customer:
            request.session['customer_id'] = customer.id
            return redirect('book_list')

    return render(request, 'login.html')
