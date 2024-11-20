from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_page, name='homepage'),
    path('contact_thank', views.contact_thank, name='contact_thank')
    
]