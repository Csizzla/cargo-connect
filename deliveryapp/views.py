
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from deliveryapp.models import Contact, Member, Order
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
        print("Orders:", orders)

        return redirect('/quote')
    else:
        return render(request,'get-a-quote.html')


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

def accounts(request):
    return render(request,'account.html')

def register(request):
    if request.method == 'POST':
        members = Member(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def customer_dashboard(request):
    # Assuming `members` is related to a user or customer
      # Replace this based on your user model setup
    customer = request.user  # Or another way to identify the logged-in customer
    orders = Order.objects.all()
    return render(request, "account.html", context = {"orders": orders,} )


  # Add this in the view and check the console
