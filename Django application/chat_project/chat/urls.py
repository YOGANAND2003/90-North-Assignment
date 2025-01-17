from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.chat_home, name='chat_home'),
    path('chat/<str:username>/', views.chat_view, name='chat_view'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
