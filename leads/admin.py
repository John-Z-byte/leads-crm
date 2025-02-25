from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'mrn', 'date_added', 'lead_type', 'tier', 'lead_owner', 'status')
    search_fields = ('patient_name', 'mrn', 'lead_owner')
    list_filter = ('lead_type', 'tier', 'status')
    ordering = ('-date_added',)  # Newest leads first

admin.site.register(Lead, LeadAdmin)
