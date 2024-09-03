from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# CarMake Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # __str__ method to return car make name
    def __str__(self):
        return self.name

# CarModel Model
class CarModel(models.Model):
    # ForeignKey to CarMake (Many-to-One relationship)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    # Car Type with limited choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # Dealer ID (integer) - refers to dealer in Cloudant database
    dealer_id = models.IntegerField()

    # Year of the model with validation
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    # __str__ method to return the car make and model name
    def __str__(self):
        return f"{self.car_make.name} {self.name}"
