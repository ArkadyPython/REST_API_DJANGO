from django.db import models


class Sensor(models.Model):

    name = models.TextField()
    description = models.TextField()

class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()

