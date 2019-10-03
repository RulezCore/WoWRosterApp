from django.contrib import admin
from .models import Member, Raid, RaidAssistance

# Register your models here.
admin.site.register(Member)
admin.site.register(Raid)
admin.site.register(RaidAssistance)