from rest_framework import serializers
from .models import Database

class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'

class DatabaseGradevsDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ['grade', 'ndays_act', 'yob']

class NotaIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ['grade', 'gender', 'loe_di']
