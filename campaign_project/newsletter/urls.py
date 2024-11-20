from django.urls import path
from . import views



urlpatterns = [
    path('', views.signup_newsletter, name='signup'),
    path('donate', views.donate, name='donate'),
     path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('get_involve', views.get_involved, name='get_involve'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path(' Donate_home', views.Donate_home,name= 'Donate_home'),
    path('thank_donation', views.thank_donation, name='thank_donation'),

]
