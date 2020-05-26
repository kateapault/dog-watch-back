import datetime
import math

from django.db import models
from django.utils import timezone

class Dog(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.CharField(max_length=10)
    breed = models.CharField(max_length=40)
    # picture = models.ImageField
    
    
    def __str__(self):
        return self.name
    
    
    # def age(self):
    #     today = datetime.date.today()
    #     age_in_days = today - self.birthday
    #     age_in_years = math.floor(age_in_days / datetime.timedelta(days=365))
    #     return age_in_years
    #     return self.birthday
    
class Food(models.Model):
    when = models.DateTimeField
    amount_value = models.FloatField
    amount_measurement = models.CharField(max_length=15)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

class Treat(models.Model):
    when = models.DateTimeField
    treat_type = models.CharField(max_length=25)
    amount_value = models.FloatField
    amount_measurement = models.CharField(max_length=15)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

class Out(models.Model):
    when = models.DateTimeField
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )
    
class Walkie(models.Model):
    when = models.DateTimeField
    distance_value = models.FloatField
    distance_measurement = models.CharField(max_length=2)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

# class Pee(models.Model):
#     when = models.DateTimeField
#         dog = models.ForeignKey(
#         Dog,
#         on_delete=models.CASCADE
#     )
