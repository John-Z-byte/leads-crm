from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadForm

# Home View
def home(request):
    leads = Lead.objects.all()
    return render(request, 'leads/home.html', {'leads': leads})

# Add Lead View
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LeadForm()
    return render(request, 'leads/add_lead.html', {'form': form})

