from rest_framework import generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorCreateView(generics.CreateAPIView):
    serializer_class = SensorDetailSerializer


class MeasurementListCreateView(generics.ListCreateAPIView):
    # queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementCreateView(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
