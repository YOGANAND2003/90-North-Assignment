from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('chat/signup/')),  # Redirect root URL
    path('chat/', include('chat.urls')),  # Include app URLs
]
