from django.urls import path
from .views import home, add_lead

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_lead, name='add-lead'),
]
