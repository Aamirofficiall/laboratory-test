from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status
from .permission import *
from .models import *
from .ser import *

class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestReportSerializer
    queryset = TestReport.objects.all()
    permission_classes = [IsOwner]
    # authentication = (TokenAuthentication,) #type of authentication, tuple


 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
