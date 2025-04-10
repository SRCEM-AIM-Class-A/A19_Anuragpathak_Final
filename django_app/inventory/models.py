from django.db import models

class Vehicle(models.Model):
    TYPE_CHOICES = [('Car', 'Car'), ('Bike', 'Bike')]
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"
