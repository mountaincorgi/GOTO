from django.contrib import admin

from .models import Profile, Friendship, Message


admin.site.register(Profile)
admin.site.register(Friendship)
admin.site.register(Message)
