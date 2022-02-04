from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Couch, Payment, Customer
from .forms import CustomerForm, CouchForm, PaymentForm
import datetime
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'customers/index.html')


def customers(request):
    customers = Customer.objects.filter(is_active=True)
    return render(
        request, 
        'customers/customers.html', 
        {'customers': customers})


def old_customers(request):
    customers = Customer.objects.filter(is_active=False)
    return render(
        request, 
        'customers/customers.html', 
        {'customers': customers})


def customer_detail(request, c_pk):
    customer = get_object_or_404(Customer, pk=c_pk)
    payment_required = Customer.objects.filter(pk=c_pk).filter(payment__month_is_paid__lte=datetime.datetime.now().month)
    created_by_month = Customer.objects.get(pk=c_pk).created_by.month
    customer_age = (customer.age if customer.age else 0) + datetime.datetime.now().year - customer.created_by.year
    need_to_pay = False
    if (len(payment_required) + created_by_month if payment_required else 0)  < datetime.datetime.now().month:
        need_to_pay = True
    return render(
        request, 
        'customers/customer_detail.html', 
            {'customer': customer, 'need_to_pay': need_to_pay, 'age': customer_age})


def payments(request, c_pk):
    customer = get_object_or_404(Customer, pk=c_pk)
    payments = Payment.objects.filter(customer__pk=c_pk)
    total = 0
    for i in (payments if payments else []):
        total += i.value_of_payment
    return render(
        request, 
        'customers/payments.html', 
        {'payments': payments, 'customer': customer, 'total': total})

@login_required
def payment_add(request, c_pk):
    data = {'customer': Customer.objects.get(pk=c_pk), 'month_is_paid': datetime.datetime.now().month, 'value_of_payment': Customer.objects.get(pk=c_pk).tariff}
    form = PaymentForm(data)
    if request.method == 'GET':
        return render(request, 'customers/payment_add.html', {'form': form, 'customer': data['customer']})
    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'customers/payment_add.html', {'form': form})
        return redirect('customer_detail', c_pk)

@login_required
def customer_update(request, c_pk):
    data = get_object_or_404(Customer, pk=c_pk)
    form = CustomerForm(instance=data)
    if request.method == 'GET':
        return render(request, 'customers/customer_update.html', {'form': form})
    else:
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'customers/customer_update.html', {'form': form})
        return redirect('customers')

@login_required
def customer_add(request):
    form = CustomerForm()
    if request.method == 'GET':
        
        return render(request, 'customers/customer_update.html', {'form': form})
    else:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'customers/customer_update.html', {'form': form})
        return redirect('customers')


def couchs(request):
    couchs = Couch.objects.filter(is_active=True)
    return render(request, 'customers/couchs.html', {'couchs': couchs})


def couch_detail(request, couch_pk):
    couch = get_object_or_404(Couch, pk=couch_pk)
    customers = Customer.objects.filter(couch=couch)
    customer_count = customers.count()

    return render(request, 'customers/couch_detail.html', {'couch': couch, 'customers': (customers if customers else ''), 'customer_count': customer_count})

@login_required
def couch_add(request):
    if request.method == 'GET':
        form = CouchForm()
        return render(request, 'customers/couch_add.html', {'form': form})
    else:
        form = CouchForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'customers/couch_add.html', {'form': form})
        return redirect('couchs')


def delayed_payment(request):
    qurent_date = datetime.datetime.now()
    delayed_payment = Customer.objects.filter(created_by__year__gte=qurent_date.year).exclude(payment__month_is_paid__lte=qurent_date.month)
    return render(request, 'customers/need_to_pay.html', {'delayed_payment': delayed_payment})