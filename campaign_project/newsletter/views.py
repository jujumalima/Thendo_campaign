from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.translation import gettext as _
from .models import NewsletterSubscriber
from django.contrib.auth import authenticate, login


def get_involved(request):
  
    return render(request, 'Donations/involve.html')

def signup_newsletter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(name=name, email=email)
                messages.success(request, 'Thank you for signing up!')
                return redirect('thank_you')  # Redirect to thank you page
            else:
                messages.warning(request, 'This email is already subscribed.')
                return redirect('signup')
        else:
            messages.error(request, 'Please provide both name and email.')

    return render(request, 'newsletter/signup.html')

def donate(request):
    return render(request, 'Donations/donate.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, _('Login successful!'))
            return redirect('Donate_home')  
        else:
            messages.error(request, _('Invalid username or password.'))
    return render(request, 'Donations/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #validation
        if not username or not email or not password:
            messages.error(request, _('All fields are required.'))
            return redirect('register')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, _('Username already exists.'))
            return redirect('register')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, _('Email already registered.'))
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log the user in
        login(request, user)
        messages.success(request, _('Registration successful! You are now logged in.'))
        return redirect('login') 

  
  
    return render(request, 'Donations/register.html')


def thank_you_view(request):
  
    return render(request, 'newsletter/thank_you.html')

def Donate_home(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Basic validation
        if not amount or not name or not email:
            messages.error(request, 'All fields are required.')
            return redirect('donate_home')

        try:
            amount = float(amount)
            if amount <= 0:
                messages.error(request, 'Please enter a valid donation amount.')
                return redirect('donate_home')
        except ValueError:
            messages.error(request, 'Please enter a valid number for the donation amount.')
            return redirect('donate_home')

        # Store data in the session
        request.session['donation_name'] = name
        request.session['donation_amount'] = amount

        messages.success(request, 'Thank you for your donation!')
        return redirect('thank_donation')  # Redirect to the thank you page

    return render(request, 'Donations/donate_home.html')



def thank_donation(request):
    
    name = request.session.get('donation_name', 'Friend')  
    amount = request.session.get('donation_amount', '0.00')  

    # Clear the session values after using them
    if 'donation_name' in request.session:
        del request.session['donation_name']
    if 'donation_amount' in request.session:
        del request.session['donation_amount']

    return render(request, 'Donations/thank_donation.html', {
        'name': name,
        'amount': amount,
    })

  


