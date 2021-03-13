
from rest_framework import serializers
from .models import *


class TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = [
            'id', 'patientName', 'raterName', 'date_created', 'grasp_score', 'grip_score','pinch_score','gross_score',]