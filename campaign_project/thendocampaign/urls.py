from django.urls import path
from . import views

"""
URL configuration for the Home application.

This module maps URL patterns to their corresponding view functions 
in the `views` module.
"""

urlpatterns = [
    path('', views.home_page, name='homepage'),  # Home page displaying news and events
    path('contact_thank', views.contact_thank, name='contact_thank'),  # Thank-you page for contact form submissions
]
