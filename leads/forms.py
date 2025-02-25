from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['hour', 'patient_name', 'mrn', 'dob', 'number', 
                  'patient_responsibility', 'tier', 'insurance_company', 
                  'lead_type', 'status', 'notes']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'hour': forms.TimeInput(attrs={'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'lead_type': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
