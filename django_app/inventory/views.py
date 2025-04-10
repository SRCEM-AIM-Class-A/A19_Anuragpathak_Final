from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm

def home(request):
    vehicles = Vehicle.objects.all()
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html', {'vehicles': vehicles, 'form': form})
