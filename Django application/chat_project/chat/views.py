from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q
from django.urls import reverse

# Home view
def home_view(request):
    return render(request, 'chat/home.html')

# Chat view (for a specific user)
def chat_view(request, username):
    selected_user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=selected_user)) |
        (Q(sender=selected_user) & Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('message')
        Message.objects.create(sender=request.user, receiver=selected_user, content=content)

    context = {
        'selected_user': selected_user,
        'messages': messages,
    }
    return render(request, 'chat/chat_room.html', context)

# Chat home (for listing users to chat with)
@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/home.html', {'users': users})

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat_home')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat_home')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
