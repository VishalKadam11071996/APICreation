from rest_framework import serializers
from .models import PatientsModel
from django.db.models import fields


class PatientsSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientsModel
		fields = '__all__'
