from django.contrib import admin

from .models import Goal, Milestone, Update


admin.site.register(Goal)
admin.site.register(Milestone)
admin.site.register(Update)
