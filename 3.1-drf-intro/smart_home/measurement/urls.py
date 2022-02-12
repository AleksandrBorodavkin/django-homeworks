from django.urls import path

from measurement.views import SensorListView, SensorUpdateView, SensorCreateView, MeasurementCreateView, \
    MeasurementRetrieveUpdateView, MeasurementListCreateView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensors-list'),
    path('sensor-update/<pk>', SensorUpdateView.as_view(), name='sensor-update'),
    path('sensor-create/', SensorCreateView.as_view(), name='sensor-create'),

    path('measurement-create/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('measurement-update/<pk>', MeasurementRetrieveUpdateView.as_view(), name='measurement-update'),
    path('measurements/', MeasurementListCreateView.as_view(), name='measurements'),

]
