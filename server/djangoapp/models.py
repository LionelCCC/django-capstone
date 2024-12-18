# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the car make")
    description = models.TextField(help_text="Description of the car make")

    def __str__(self):
        return self.name
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        # Add more choices as needed
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")  # Many-to-One relationship
    name = models.CharField(max_length=100, help_text="Name of the car model")
    car_type = models.CharField(max_length=10, choices=CAR_TYPES, default=SUV, help_text="Type of the car model")
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        help_text="Year of manufacture"
    )
    dealer_id = models.IntegerField(help_text="ID of the dealer associated with this car model")
    # Add other fields if needed

    def __str__(self):
        return f"{self.car_make.name} - {self.name} ({self.car_type}, {self.year})"  # String representation of CarModel
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
