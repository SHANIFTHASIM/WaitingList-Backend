from django.contrib import admin

from Authuser.models import WaitlistEntry

# Register your models here.
class AdminWaitlistEntry(admin.ModelAdmin):
    list_display=("email","timestamp")

admin.site.register(WaitlistEntry, AdminWaitlistEntry)