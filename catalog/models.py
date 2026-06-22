from django.db import models

class Pipe(models.Model):
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=100)
    diameter_mm = models.PositiveIntegerField()
    wall_thickness_mm = models.DecimalField(max_digits=6, decimal_places=2)
    max_pressure_bar = models.DecimalField(max_digits=8, decimal_places=2)
    weight_per_meter = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.diameter_mm} мм'

class Valve(models.Model):
    name = models.CharField(max_length=200)
    valve_type = models.CharField(max_length=100)
    diameter_mm = models.PositiveIntegerField()
    max_pressure_bar = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.diameter_mm} мм'
