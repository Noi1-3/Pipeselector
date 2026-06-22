import math
from django.shortcuts import get_object_or_404, render
from .forms import SelectionForm
from .models import Pipe, Valve

def home(request):
    return render(request, 'catalog/home.html')

def calculator(request):
    form = SelectionForm(request.GET or None)
    results = []

    if form.is_valid():
        flow_rate = float(form.cleaned_data['flow_rate'])
        pressure = float(form.cleaned_data['pressure'])

        q = flow_rate / 3600
        pipes = Pipe.objects.filter(max_pressure_bar__gte=pressure).order_by('diameter_mm')

        for pipe in pipes:
            area = math.pi * (pipe.diameter_mm / 1000) ** 2 / 4
            velocity = q / area

            if 0.5 <= velocity <= 3:
                valves = Valve.objects.filter(
                    diameter_mm=pipe.diameter_mm,
                    max_pressure_bar__gte=pressure
                ).order_by('name')

                results.append({
                    'pipe': pipe,
                    'velocity': round(velocity, 3),
                    'valves': valves
                })

    return render(request, 'catalog/calculator.html', {'form': form, 'results': results})

def pipe_list(request):
    pipes = Pipe.objects.all().order_by('diameter_mm')
    return render(request, 'catalog/pipe_list.html', {'pipes': pipes})

def valve_list(request):
    valves = Valve.objects.all().order_by('diameter_mm')
    return render(request, 'catalog/valve_list.html', {'valves': valves})

def pipe_detail(request, id):
    pipe = get_object_or_404(Pipe, id=id)
    valves = Valve.objects.filter(
        diameter_mm=pipe.diameter_mm,
        max_pressure_bar__gte=pipe.max_pressure_bar
    ).order_by('name')
    return render(request, 'catalog/pipe_detail.html', {'pipe': pipe, 'valves': valves})

def valve_detail(request, id):
    valve = get_object_or_404(Valve, id=id)
    return render(request, 'catalog/valve_detail.html', {'valve': valve})