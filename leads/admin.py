from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name', 
        'mrn', 
        'insurance_company', 
        'lead_type', 
        'tier', 
        'status', 
        'date_added'
    )
    search_fields = ('patient_name', 'mrn', 'insurance_company', 'number')
    list_filter = ('lead_type', 'tier', 'status', 'date_added')
    ordering = ('-date_added',)
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient_name', 'mrn', 'dob', 'number')
        }),
        ('Lead Details', {
            'fields': ('hour', 'patient_responsibility', 'tier', 'insurance_company', 'lead_type', 'status', 'lead_owner')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
    )

admin.site.register(Lead, LeadAdmin)

