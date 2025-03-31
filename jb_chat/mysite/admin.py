from django.contrib import admin
from mysite.models import Message, ChatRoom, Avatar, UserProfile

admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(Avatar)
admin.site.register(UserProfile)
