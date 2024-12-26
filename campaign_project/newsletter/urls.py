from django.urls import path
from . import views

"""
URL configuration for the Donations application.

This module maps URLs to their respective view functions, facilitating navigation
and interaction within the application.

Routes:
    - signup: Newsletter signup form
    - donate: Donation form
    - login: User login page
    - register: User registration page
    - get_involve: Get Involved page
    - thank_you: Thank You page for newsletter signup
    - Donate_home: Donation Home page
    - thank_donation: Thank You page for donation
"""

urlpatterns = [
    path('', views.signup_newsletter, name='signup'),  # Newsletter signup form
    path('donate/', views.donate, name='donate'),  # Donation form
    path('login/', views.login_view, name='login'),  # User login page
    path('register/', views.register_view, name='register'),  # User registration page
    path('get_involve/', views.get_involved, name='get_involve'),  # Get Involved page
    path('thank-you/', views.thank_you_view, name='thank_you'),  # Thank You page
    path('Donate_home/', views.Donate_home, name='Donate_home'),  # Donation Home page
    path('thank_donation/', views.thank_donation, name='thank_donation'),  # Donation Thank You page
]
