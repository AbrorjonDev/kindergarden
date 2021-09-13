from rest_framework import serializers
from .models import *


class TumanS(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = '__all__'


class KGS(serializers.ModelSerializer):
    class Meta:
        model = KG
        fields = '__all__'


class TadbirS(serializers.ModelSerializer):
    class Meta:
        model = Tadbir
        fields = '__all__'


class YangilikS(serializers.ModelSerializer):
    class Meta:
        model = Yangilik
        fields = "__all__"
    

class RahbariyatS(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = '__all__'
