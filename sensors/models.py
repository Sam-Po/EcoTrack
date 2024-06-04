from django.db import models
from django.contrib.auth.models import User


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='sensors', on_delete=models.CASCADE)


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pm2_5 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()
