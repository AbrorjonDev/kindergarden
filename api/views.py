from rest_framework.generics import *
from .serializer import *


class TumanCV(ListCreateAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanS


class TumanUV(RetrieveUpdateDestroyAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanS


class KGCV(ListCreateAPIView):
    queryset = KG.objects.all()
    serializer_class = KGS


class KGUV(RetrieveUpdateDestroyAPIView):
    queryset = KG.objects.all()
    serializer_class = KGS


class TadbirCV(ListCreateAPIView):
    queryset = Tadbir.objects.all()
    serializer_class = TadbirS


class TadbirUV(RetrieveUpdateDestroyAPIView):
    queryset = Tadbir.objects.all()
    serializer_class = TadbirS


class YangilikCV(ListCreateAPIView):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikS


class YangilikUV(RetrieveUpdateDestroyAPIView):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikS


class RahbariyatCV(ListCreateAPIView):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatS


class RahbariyatUV(UpdateAPIView):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatS
