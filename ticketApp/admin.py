from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('status', 'assignee','department')
	list_display = ('id', 'title', 'status', 'assignee', 'department','description', 'updated_at')
	search_fields = ['title','status']

admin.site.register(Ticket, TicketAdmin)