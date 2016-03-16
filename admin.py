from django.contrib import admin

# Register your models here.
from .models import dns_records

class dns_recordsAdmin(admin.ModelAdmin):
	list_display = ['zone','host','type','data','ttl','mx_priority','refresh','retry','expire','minimum','serial','resp_person','primary_ns']
	list_filter = ['host','data']
	search_fields = ['host','data']

admin.site.register(dns_records,dns_recordsAdmin)
