from django.db import models


# Create your models here.

class Bus(models.Model):
    MAKE_TYPE = (
        ('MB', 'Mercedes Benz'),
    )

    MODEL_TYPE = (
        ('VI', 'Vito'),
    )

    GEAR_TYPE = (
        ('AU', 'Automatic'),
        ('MA', 'Manual')
    )

    CHASSIS_TYPE = (
        ('SH', 'Short'),
        ('ME', 'Medium'),
        ('TA', 'Tall')
    )

    CAPACITY_TYPE = (
        ('VAN', 'VAN'),
        ('MIX', 'MIXTO')
    )

    FUEL_TYPE = (
        ('BE', 'Benzene'),
        ('DI', 'Diesel')
    )

    make = models.CharField(max_length=2, choices=MAKE_TYPE)
    model = models.CharField(max_length=2, choices=MODEL_TYPE)
    year = models.PositiveIntegerField()
    gear = models.CharField(max_length=2, choices=GEAR_TYPE)
    chassis = models.CharField(max_length=2, choices=CHASSIS_TYPE)
    mileage = models.PositiveIntegerField()
    horse_power = models.PositiveIntegerField()
    features = models.TextField()
    capacity = models.CharField(max_length=3, choices=CAPACITY_TYPE)
    fuel = models.CharField(max_length=2, choices=FUEL_TYPE)
    location = models.CharField(max_length=200)
    price = models.FloatField()
    color = models.CharField(max_length=200)
    chassis_number = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    store_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.get_make_display() + ' ' + str(self.get_model_display()) + ' ' + str(self.horse_power) + ' ' + str(
            self.year)

    def title(self):
        return self.get_make_display() + ' ' + str(self.get_model_display()) + ' ' + str(self.horse_power) + ' ' + str(
            self.year)
