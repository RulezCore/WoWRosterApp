from django.contrib import admin
from .models import Member, Raid, RaidAssistance

class RaidAssistanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'assistance')

# Register your models here.
admin.site.register(Member)
admin.site.register(Raid)
admin.site.register(RaidAssistance, RaidAssistanceAdmin)