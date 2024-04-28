from rest_framework import serializers
from .models import Database

class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'

class DatabaseGradevsDaysSerializer(serializers.ModelSerializer):
    ndays_act = serializers.SerializerMethodField()

    class Meta:
        model = Database
        fields = ['grade', 'ndays_act', 'yob']

    def get_ndays_act(self, obj):
        if obj.ndays_act is not None:
            return obj.ndays_act
        else:
            return 0
        

