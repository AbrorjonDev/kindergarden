from rest_framework import serializers
from .models import *
from rest_framework.response import Response


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


class XodimS(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = '__all__'


class PasswordResetSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return Response(status=201)
