from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ChatRoom, Message, UserProfile, User, Avatar
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
    up = UserProfile.objects.filter(user=user)
    ava = Avatar.objects.filter(userprofile=up[0])
    if ava:
        av = ava[0].file_location
        return render(request, "welcome.html", {"user": user, "av": av})
    else:
        default_avatar = "avatars\\avatar.png"
        return render(request, "welcome.html", {"user": user, "av": default_avatar})


@login_required
def chat_room(request, room_name):
    user = request.user
    room = get_object_or_404(ChatRoom, name=room_name)
    cr = ChatRoom.objects.filter(users = user)
    users = room.users.all()
    avs = []
    if not room.users.filter(id=user.id).exists():
        raise Http404("You are not a member of this chat room.")
    
    messages = Message.objects.filter(room=room).order_by('timestamp')
    for us in users:
        u = {}
        up = UserProfile.objects.filter(user=us)
        ava = Avatar.objects.filter(userprofile=up[0])
        u["user"] = us.username
        if ava:
            u["avatar"] = ava[0].file_location
            
        else:
            u['avatar'] = 'avatars/avatar.png'
        avs.append(u)
    
    return render(request, 'chat.html', {'room_name': room_name, 'user': user, 'messages': messages, "chatrooms": cr, "avs": avs})


@login_required
def chat(request):
    user = request.user
    cr = ChatRoom.objects.filter(users = user)
    up = UserProfile.objects.filter(user=user)
    ava = Avatar.objects.filter(userprofile=up[0])
    avs = []
    if ava:
        u = {}
        u["user"] = user.username
        u["avatar"] = ava[0].file_location
        avs.append(u)
        return render(request, 'chat.html', {'user': user, "chatrooms": cr, "avs": avs})
    else:
       u = {"user": user.username}
       u['avatar'] = 'avatars/avatar.png'
       avs.append(u)
       return render(request, 'chat.html', {'user': user, "chatrooms": cr, "avs": avs})
    


@login_required
def default_route(request):
    return redirect ('welcome')