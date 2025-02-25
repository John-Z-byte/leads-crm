from django.db import models

class Lead(models.Model):
    hour = models.TimeField()
    patient_name = models.CharField(max_length=100)
    mrn = models.CharField(max_length=50, unique=True)
    dob = models.DateField()
    number = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)
    patient_responsibility = models.DecimalField(max_digits=10, decimal_places=2)
    tier = models.CharField(max_length=10, choices=[('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3')])
    insurance_company = models.CharField(max_length=100)
    lead_type = models.CharField(max_length=50)
    lead_owner = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.mrn}"
