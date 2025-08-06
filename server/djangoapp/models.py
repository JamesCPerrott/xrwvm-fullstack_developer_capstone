from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        # Return the name as the string representation
        return self.name


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('CARGO VAN', 'Cargo Van'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe'),
        ('CROSSOVER', 'Crossover'),
        ('HATCHBACK', 'Hatchback'),
        ('MINIVAN', 'Minivan'),
        ('PASSENGER VAN', 'Passenger Van'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('TRUCK', 'Truck'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=13, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
    )
    CAR_COLORS = [
        ('BLACK', 'Black'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('GRAY', 'Gray'),
        ('GREEN', 'Green'),
        ('GOLD', 'Gold'),
        ('ORANGE', 'Orange'),
        ('RED', 'Red'),
        ('SILVER', 'Silver'),
        ('WHITE', 'White'),
        ('YELLOW', 'Yellow'),
    ]
    color = models.CharField(max_length=8, choices=CAR_COLORS, default='RED')

    def __str__(self):
        # Return the name as the string representation
        return self.name
