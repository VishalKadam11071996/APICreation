from django.shortcuts import render

# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import PatientsSerializer
from .models import PatientsModel


# create a viewset
class PatientsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = PatientsModel.objects.all()

    # specify serializer to be used
    serializer_class = PatientsSerializer
