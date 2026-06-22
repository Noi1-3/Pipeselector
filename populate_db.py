import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PipeSelector.settings')
django.setup()

from catalog.models import Pipe, Valve

def populate():
    Pipe.objects.all().delete()
    Valve.objects.all().delete()

    pipes_data = [
        {"name": "Труба ВГП ГОСТ 3262-75", "material": "Сталь углеродистая", "diameter_mm": 50, "wall_thickness_mm": 3.0, "max_pressure_bar": 16.0, "weight_per_meter": 4.88},
        {"name": "Труба ВГП ГОСТ 3262-75", "material": "Сталь углеродистая", "diameter_mm": 100, "wall_thickness_mm": 4.0, "max_pressure_bar": 16.0, "weight_per_meter": 10.8},
        {"name": "Труба PE 100 SDR 11", "material": "Полиэтилен", "diameter_mm": 50, "wall_thickness_mm": 4.6, "max_pressure_bar": 16.0, "weight_per_meter": 0.67},
        {"name": "Труба PE 100 SDR 17", "material": "Полиэтилен", "diameter_mm": 100, "wall_thickness_mm": 6.6, "max_pressure_bar": 10.0, "weight_per_meter": 1.95},
        {"name": "Труба бесшовная ГОСТ 8732-78", "material": "Сталь 09Г2С", "diameter_mm": 150, "wall_thickness_mm": 6.0, "max_pressure_bar": 40.0, "weight_per_meter": 21.3},
    ]

    valves_data = [
        {"name": "Кран шаровый фланцевый КШ.Ф", "valve_type": "Шаровый кран", "diameter_mm": 50, "max_pressure_bar": 40.0, "weight": 4.5},
        {"name": "Задвижка клиновая 30с41нж", "valve_type": "Задвижка", "diameter_mm": 50, "max_pressure_bar": 16.0, "weight": 18.0},
        {"name": "Кран шаровый фланцевый КШ.Ф", "valve_type": "Шаровый кран", "diameter_mm": 100, "max_pressure_bar": 16.0, "weight": 14.2},
        {"name": "Затвор дисковый Баттерфляй", "valve_type": "Поворотный затвор", "diameter_mm": 100, "max_pressure_bar": 16.0, "weight": 5.1},
        {"name": "Задвижка стальная 30с15нж", "valve_type": "Задвижка", "diameter_mm": 150, "max_pressure_bar": 40.0, "weight": 75.0},
    ]

    for p in pipes_data:
        Pipe.objects.create(**p)

    for v in valves_data:
        Valve.objects.create(**v)

if __name__ == '__main__':
    populate()