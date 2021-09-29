from rest_framework.generics import *
from .serializers import *
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.response import Response
from api.serializers import PasswordResetSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from dj_rest_auth.registration.views import APIView, ConfirmEmailView, AllowAny, MethodNotAllowed, status

#
# class TumanCV(ListCreateAPIView):
#     queryset = Tuman.objects.all()
#     serializer_class = TumanS
#
#
# class TumanUV(RetrieveUpdateDestroyAPIView):
#     queryset = Tuman.objects.all()
#     serializer_class = TumanS


class KGCV(ListCreateAPIView):
    queryset = KG.objects.all()
    serializer_class = KGS

class AllDataView(APIView):
    queryset = KG.objects.all()
    serializer_class = IDS

    def get_object(self, pk):
        return KG.objects.get(pk=pk)

    def post(self, request, format=None):
        pk = request.data['id']
        object = self.get_object(pk)
        rahbariyat = Rahbariyat.objects.filter(kg=object)
        xodim = Xodim.objects.filter(kg=object)
        tadbir = Tadbir.objects.filter(kg=object)
        yangilik = Yangilik.objects.filter(kg=object)
        post = Post.objects.filter(kg=object)
        menu = Menu.objects.filter(kg=object)
        media = Image_Video.objects.filter(kg=object)
        serializer = {
            'rahbariyat': RahbariyatS(rahbariyat, many=True).data,
            'xodim': XodimS(xodim, many=True).data,
            'tadbir': TadbirS(tadbir, many=True).data,
            'yangilik': YangilikS(yangilik, many=True).data,
            'post': PostS(post, many=True).data,
            'menu': MenuSerializer(menu, many=True).data,
            'media': ImageVideoSerializer(media, many=True).data,
        }
        serializer["id"] = object.id
        serializer["name"] = object.name
        serializer["email"] = object.email
        serializer["tuman"] = object.tuman
        serializer["number"] = object.number
        serializer["address"] = object.address
        serializer["tel"] = object.tel
        serializer["telegram"] = object.telegram
        serializer["logo"] = object.logo.url
        return Response(serializer, status=200)




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

class XodimCV(ListCreateAPIView):
    queryset = Xodim.objects.all()
    serializer_class = XodimS


class XodimUV(UpdateAPIView):
    queryset = Xodim.objects.all()
    serializer_class = XodimS


class PostCV(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostS

class PostUV(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostS

class MediaCV(ListCreateAPIView):
    queryset = Image_Video.objects.all()
    serializer_class = ImageVideoSerializer

class MediaUV(RetrieveUpdateDestroyAPIView):
    queryset = Image_Video.objects.all()
    serializer_class = ImageVideoSerializer

class MenuView(APIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self, request, *args):
        serializer = self.serializer_class(Menu.objects.all(), many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors)

    # def put(self, request, pk):
    #     self.get_object()
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         Menu
    #         serializer.save()
    #         return Response()
class MenuUV(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

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