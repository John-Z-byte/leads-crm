from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Returned', 'Returned'),
    ]

    LEAD_TYPE_CHOICES = [
        ('HST', 'HST'),
        ('MCT', 'MCT'),
    ]

    hour = models.TimeField()
    patient_name = models.CharField(max_length=100)
    mrn = models.CharField(max_length=50, unique=True)
    dob = models.DateField()
    number = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)
    patient_responsibility = models.DecimalField(max_digits=10, decimal_places=2)
    tier = models.CharField(max_length=10, choices=[
        ('0-75 $', '0-75 $'),
        ('76-199 $', '76-199 $'),
        ('200-329 $', '200-329 $')
    ])
    insurance_company = models.CharField(max_length=100)
    lead_type = models.CharField(max_length=10, choices=LEAD_TYPE_CHOICES)
    lead_owner = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='New')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.mrn}"

