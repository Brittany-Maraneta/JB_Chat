from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ChatRoom, Message, UserProfile
from django.http import Http404

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
    room = get_object_or_404(ChatRoom, name=room_name)
    cr = ChatRoom.objects.filter(users = user)
    if not room.users.filter(id=user.id).exists():
        raise Http404("You are not a member of this chat room.")
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat.html', {'room_name': room_name, 'user': user, 'messages': messages, "chatrooms": cr })


@login_required
def chat(request):
    user = request.user
    cr = ChatRoom.objects.filter(users = user)
    up = UserProfile.objects.filter(user = user) 
    av = up[0].avatar
    
    
    return render(request, 'chat.html', {'user': user, "chatrooms": cr, "av": av})

@login_required
def default_route(request):
    return redirect ('welcome')