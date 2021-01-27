from rest_framework import serializers, viewsets, routers

from providers.serializers import EmployeeSerializer
from providers.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
