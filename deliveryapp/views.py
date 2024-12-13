from idlelib.rpc import request_queue
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from deliveryapp.models import Contact, Member, Order, Feedback
from deliveryapp.forms import OrderForm
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
            ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')


def quote(request):
    if request.method == "POST":
        orders=Order(
            departure_city = request.POST['departure'],
            delivery_city = request.POST['delivery'],
            weight = request.POST['weight'],
            dimensions = request.POST['dimensions'],
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message'],
        )
        orders.save()

        return redirect('/quote')
    else:
        return render(request,'get-a-quote.html')

def feedback(request):
    if request.method == 'POST':
        feedbacks=Feedback(
            message=request.POST['message'],
        )
        feedbacks.save()
        return redirect('/account')
    else:
        return render(request,'account.html')


def contact(request):
    if request.method == "POST":
        mycontact=Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def register(request):
    if request.method == 'POST':

        member = Member(
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        member.save()

        return redirect('/login')

    return render(request, 'register.html')





def account(request):
    orders = Order.objects.all()


    return render(request,'account.html',{'orders':orders})


def delete(request, id):
    orders=Order.objects.get(id=id)
    orders.delete()
    return redirect('/account')

def edit(request, id):
    editorders = Order.objects.get(id=id)

    return render(request,'edit.html',{'orders':editorders})

def update(request,id):
    updateinfo=Order.objects.get(id=id)
    form=OrderForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/account')
    else:
        return render(request,'edit.html')


def accept(request):
    orders = Order.objects.all()
    return render(request, 'accounts.html',{'orders':orders})

    