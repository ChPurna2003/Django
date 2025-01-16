from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message  # Import the Message model
from django.db.models import Q  # Import Q for complex queries

def room(request, room_name, username=None):
    users = User.objects.all()  # Fetch all registered users
    messages = []  # Initialize messages list

    if username:
        # Fetch messages between the logged-in user and the selected user
        messages = Message.objects.filter(
            Q(sender=request.user, recipient__username=username) |
            Q(sender__username=username, recipient=request.user)
        ).order_by('timestamp')  # Order messages by timestamp

    return render(request, 'chat/chat.html', {
        'room_name': room_name,
        'users': users,
        'messages': messages,
    })