
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from deliveryapp.models import Quote, Contact, Member
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if both fields are provided
        if email and password:
            try:
                user = Member.objects.get(email=email)
                if check_password(password, user.password):
                    # Login successful
                    request.session['member_id'] = user.id
                    messages.success(request, f"Welcome back, {user.full_name}!")
                    return redirect('index')
                else:
                    messages.error(request, "Invalid password.")
            except Member.DoesNotExist:
                messages.error(request, "Invalid email.")
        else:
            messages.error(request, "Both email and password are required.")

        return redirect('login')  # Redirect back to the login page on failure

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
        myquote=Quote(
            departure_city = request.POST['departure'],
            delivery_city = request.POST['delivery'],
            weight = request.POST['weight'],
            dimensions = request.POST['dimensions'],
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message'],
        )
        myquote.save()
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
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']

        # Hash the password
        hashed_password = make_password(password)

        # Create and save the Member object
        member = Member(full_name=full_name, email=email, password=hashed_password)
        member.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    return render(request,'login.html')

from django.shortcuts import render

def customer_dashboard(request):
    # Sample data to display on the dashboard
    context = {
        'customer_name': 'John Jaz',
        'total_orders': 20,
        'pending_orders': 5,
        'completed_orders': 15,
        'active_deliveries': [
            {'id': 1, 'package': 'Laptop', 'status': 'In Transit', 'destination': 'New York'},
            {'id': 2, 'package': 'Furniture', 'status': 'Out for Delivery', 'destination': 'Los Angeles'},
        ],
    }
    return render(request, 'account.html', context)


