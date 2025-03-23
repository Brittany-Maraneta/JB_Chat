from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ChatRoom, Message

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'signup.html', {'form': form})

@login_required
def welcome(request):
    user = request.user
    return render(request, "welcome.html", {"user": user})


@login_required
def chat_room(request, room_name):
    user = request.user
    # Get the ChatRoom object based on the room_name
    room = ChatRoom.objects.get(name=room_name)
    
    # Get all messages for the specific room, ordered by timestamp
    messages = Message.objects.filter(room=room).order_by('timestamp')

    return render(request, 'chat.html', {
        'room_name': room_name,
        'user': user,
        'messages': messages  # Pass messages to the template
    })


@login_required
def chat(request):
    user = request.user

    return render(request, 'chat.html')

@login_required
def default_route(request):
    return redirect ('welcome')