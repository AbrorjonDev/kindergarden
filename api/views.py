from rest_framework.generics import *
from .serializers import *
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.response import Response
from api.serializers import PasswordResetSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from dj_rest_auth.registration.views import APIView, ConfirmEmailView, AllowAny, MethodNotAllowed, status


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

class PasswordResetConfirmAPIView(PasswordResetConfirmView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        path = request.path
        uid = path.split('/')[-3]
        user = User.objects.get(pk=uid)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if request.data["new_password1"] == request.data["new_password2"]:
                user.set_password(request.data["new_password1"])
                user.save()
            else:
                return Response({'detail': _('Password confirmation is wrong.')},)

            serializer.save()
        return Response(
            {'detail': _('Password has been reset with the new password.')},
        )


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    #
    # def get_serializer(self, *args, **kwargs):
    #     return VerifyTokenSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        path = request.path
        key = path.split("/")[:-3]
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)