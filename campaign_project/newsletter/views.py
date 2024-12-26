from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext as _
from .models import NewsletterSubscriber


def get_involved(request):
    """
    Renders the 'Get Involved' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'Get Involved' template.
    """
    return render(request, 'Donations/involve.html')


def signup_newsletter(request):
    """
    Handles newsletter signup requests.

    If the request method is POST, captures the user's name and email
    and saves them as a subscriber. Provides feedback via messages.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the appropriate page or renders the signup page.
    """
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
    """
    Renders the donation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered donation page.
    """
    return render(request, 'Donations/donate.html')


def login_view(request):
    """
    Handles user login requests.

    Authenticates the user and logs them in if credentials are valid.
    Provides feedback via messages.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the home page or renders the login page.
    """
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
    """
    Handles user registration requests.

    Validates user input, creates a new user, and logs them in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the login page or renders the registration page.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, _('All fields are required.'))
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.warning(request, _('Username already exists.'))
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.warning(request, _('Email already registered.'))
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        messages.success(request, _('Registration successful! You are now logged in.'))
        return redirect('login')

    return render(request, 'Donations/register.html')


def thank_you_view(request):
    """
    Renders the 'Thank You' page after newsletter signup.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'Thank You' template.
    """
    return render(request, 'newsletter/thank_you.html')


def Donate_home(request):
    """
    Handles donation requests.

    Validates input and stores donation data in the session for use
    on the thank-you page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the thank-you page or renders the donation form.
    """
    if request.method == 'POST':
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        email = request.POST.get('email')

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

        request.session['donation_name'] = name
        request.session['donation_amount'] = amount

        messages.success(request, 'Thank you for your donation!')
        return redirect('thank_donation')

    return render(request, 'Donations/donate_home.html')


def thank_donation(request):
    """
    Renders the 'Thank You for Donation' page.

    Retrieves and clears donation details from the session.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered thank-you page with donation details.
    """
    name = request.session.get('donation_name', 'Friend')
    amount = request.session.get('donation_amount', '0.00')

    if 'donation_name' in request.session:
        del request.session['donation_name']
    if 'donation_amount' in request.session:
        del request.session['donation_amount']

    return render(request, 'Donations/thank_donation.html', {
        'name': name,
        'amount': amount,
    })
