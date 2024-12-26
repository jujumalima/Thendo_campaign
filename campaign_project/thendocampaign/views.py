from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News, Event  

"""
Views for the Home application.

This module provides functionality for rendering the home page and a thank-you page 
for contact form submissions. It integrates data from the News and Event models.
"""

def home_page(request):
    """
    Render the home page with the latest news and upcoming events.

    Handles the contact form submission, validates input, and displays success or error messages.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page or a redirect to the thank-you page.
    """
    # Fetch latest news and upcoming events from models
    latest_news = News.objects.order_by('-published_date')[:3]
    upcoming_events = Event.objects.order_by('date')[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Show success message and redirect
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_thank')  
        else:
            # Show error message if validation fails
            messages.error(request, 'Please fill in all fields.')

    context = {
        'latest_news': latest_news,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'Home/index.html', context)

def contact_thank(request):
    """
    Render the thank-you page for contact form submissions.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered thank-you page.
    """
    return render(request, 'Home/contact_thank.html')
