from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     # Include URLs from the 'thendocampaign' app
     path('', include('thendocampaign.urls')),  
     path('subscribe/', include('newsletter.urls')),
]
