from django.shortcuts import render, redirect

from .models import Orderrequest
from .forms import OrderForm

def order_request(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders:order_table")
    else:
        form = OrderForm()
    return render(request, 'orders/index.html', {'form': form})

def order_table(request):
    orders = Orderrequest.objects.all()
    return render(request, 'orders/pendings.html', {'orders': orders})