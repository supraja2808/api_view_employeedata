from rest_framework import serializers
from app.models import *

class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'