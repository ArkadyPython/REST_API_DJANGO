"""simple_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from measurements.views import SensorsList_or_create_ViewSet, Measurement_add_measure_ViewSet, \
    Sensor_change_measure_ViewSet, SensorViewSet

# router = routers.DefaultRouter()
# router.register('projects', measurements.views.ProjectViewSet, basename='projects')
# router.register('measures', MeasurementViewSet, basename='measures')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorsList_or_create_ViewSet.as_view()),
    path('measurements/', Measurement_add_measure_ViewSet.as_view()),
    path('sensors/update/<pk>', Sensor_change_measure_ViewSet.as_view()),
    path('sensors/<pk>', SensorViewSet.as_view())
]