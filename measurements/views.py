from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from measurements.models import Sensor, Measurement
from measurements.serializers import SensorDetailSerializer, MeasurementSerializer, SensorChangeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , UpdateAPIView , RetrieveAPIView


class SensorsList_or_create_ViewSet(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class Measurement_add_measure_ViewSet(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class Sensor_change_measure_ViewSet(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer

class SensorViewSet(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

