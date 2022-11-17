from django.db import models
#from django.countries.fields import CountryField

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=210,blank=True, null=True)
    brand = models.CharField(max_length=210,blank=True, null=True)
    provider = models.CharField(max_length=210,blank=True, null=True)
    country_of_Origin = models.CharField(max_length=210,blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.car_brand} {self.provider}'

class Provider(models.Model):
    provider = models.CharField(max_length=210, blank=True, null=True)
    creater = models.CharField(max_length=210, blank=True, null=True)
    email = models.CharField(max_length=210, blank=True, null=True)
    information_of_company = models.CharField(max_length=210, blank=True, null=True)

    def __str__(self):
        return f'{self.provider} {self.creater}'

# class Tag(models.Model):
#     provider_1 = models.CharField(max_length=210,blank=True, null=True)
#     cars = models.ManyToManyField(Car)

