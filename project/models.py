from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    MANAGER = 'MG'
    OPERATOR = 'OP'

    USER_TYPE_CHOICES = [
        (MANAGER, 'Manager'),
        (OPERATOR, 'Operator'),
    ]

    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=OPERATOR)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

class CarModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

class CityModel(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    cars = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='city_files/')

    def __str__(self):
        return self.name