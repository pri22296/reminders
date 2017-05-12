from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'date',)
    search_fields = ('user','date',)
    list_filter = ('user','date',)
    
# Register your models here.
admin.site.register(Reminder, ReminderAdmin)
