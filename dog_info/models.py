import datetime
import math

from django.db import models
from django.utils import timezone

class Dog(models.Model):
    name = models.CharField(max_length=40)
    birthdate = models.DateField(blank=True, null=True)
    breed = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
    def age(self):
        today = datetime.date.today()
        age_in_days = today - self.birthday
        age_in_years = math.floor(age_in_days / datetime.timedelta(days=365))
        return age_in_years
        return self.birthday
    
class Food(models.Model):
    when = models.DateTimeField(blank=True, null=True)
    amount_value = models.FloatField(blank=True, null=True)
    amount_measurement = models.CharField(max_length=15)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

class Treat(models.Model):
    when = models.DateTimeField(blank=True, null=True)
    treat_type = models.CharField(max_length=25)
    amount_value = models.FloatField(blank=True, null=True)
    amount_measurement = models.CharField(max_length=15)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

class Out(models.Model):
    when = models.DateTimeField(blank=True, null=True)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )
    
class Walkie(models.Model):
    when = models.DateTimeField(blank=True, null=True)
    distance_value = models.FloatField(blank=True, null=True)
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
