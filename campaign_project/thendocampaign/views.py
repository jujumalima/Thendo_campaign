from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News, Event  

def home_page(request):
    # Fetch latest news and upcoming events models
    latest_news = News.objects.order_by('-published_date')[:3]
    upcoming_events = Event.objects.order_by('date')[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_thank')  
        else:
            messages.error(request, 'Please fill in all fields.')

    context = {
        'latest_news': latest_news,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'Home/index.html', context)

def contact_thank(request):
    return render(request, 'Home/contact_thank.html')


