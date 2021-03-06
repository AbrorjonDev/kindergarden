from rest_framework.generics import *
from .serializers import *
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.response import Response
from api.serializers import PasswordResetSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from dj_rest_auth.registration.views import APIView, ConfirmEmailView, AllowAny, MethodNotAllowed, status

from dj_rest_auth.views import PasswordResetView

# class CustomPasswordResetView(PasswordResetView):
#     pass
class CustomPasswordResetView(APIView):
    serializer_class = EmailS

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            try:
                user = User.objects.get(email=email)
                code = VerifyAccountCode.objects.create(email=email, code=generate_activation_code())
                message = f'''
                    Assalomu alaykum, {email}.
                    Kimdir sizning nomingizdan parolni qayta o'rnatish so'rovini jo'natdi.
                    Agar bu siz bo'lmasangiz, bu xabarni e'tiborsiz qoldiring.
                                                  ----------
                    Sizning tasdiqlash kodingiz :| {code.code} .|
                                                  ----------
                    Sizning saytdagi nomingiz {user.username}.
                    Iltimos, bu kodni hech kimga bermang.
                '''
                send_mail(
                    "Kirish parolini o'zgartirish kodi: ",
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                raise e
        return Response({"detail": "Agar elektron pochta manzilini to\'g\'ri kiritgan bo\'lsangiz, unga tasdiqlash kodi yuborildi. "})

class CustomPasswordResetConfirmView(APIView):

    serializer_class = PasswordResetS
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(serializer.data)
            return Response({"detail":"Parol muvaffaqiyatli almashtirildi."}, status=201)
        return Response(serializer.errors, status=400)


    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         new_password1 = serializer.validated_data.get('new_password1')
    #         # uid = request.path.split('/')[-2]
    #         # token = request.path.split('/')[-1]
    #         uid = kwargs["uidb64"]
    #         token = kwargs["token"]
    #
    #         self.serializer_class.validation(self, uid=uid, token=token, new_password1=new_password1)
    #         return Response({'detail': 'parol muvaffaqiyatli almashtirildi.',})
    #     return Response({'detail': 'Xatolik sodir bo\'ldi'})
# #
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
    serializer_class = KeySerializer

    def get_object(self, key):
        try:
            email = Token.objects.get(key=key).user.email
            return get_object_or_404(KG, email=email)
        except Exception as e:
            raise e

    def post(self, request, format=None):
        serializer = KeySerializer(data=request.data)
        if serializer.is_valid():
            try:
                token = serializer.validated_data.get('key')
                object = self.get_object(token)
                rahbariyat = Rahbariyat.objects.filter(kg=object)
                xodim = Xodim.objects.filter(kg=object)
                tadbir = Tadbir.objects.filter(kg=object)
                yangilik = Yangilik.objects.filter(kg=object)
                # post = Post.objects.filter(kg=object)
                oshxona = Oshxona.objects.filter(kg=object)
                menu = []
                for o in oshxona:
                    menu += Menu.objects.filter(oshxona=o)
                media = Image_Video.objects.get(kg=object)
                serializer = {
                    'rahbariyat': RahbariyatS(rahbariyat, many=True).data,
                    'xodim': XodimS(xodim, many=True).data,
                    'tadbir': TadbirS(tadbir, many=True).data,
                    'yangilik': YangilikS(yangilik, many=True).data,
                    # 'post': PostS(post, many=True).data,
                    'oshxona': OshxonaSerializer(oshxona, many=True).data,
                    'menu': MenuSerializer(menu, many=True).data,
                    'media': ImageVideoSerializer(media, many=False).data,
                }
                serializer["id"] = object.id
                serializer["name"] = object.name
                serializer["email"] = object.email
                serializer["viloyat"] = object.viloyat
                serializer["tuman"] = object.tuman
                serializer["number"] = object.number
                serializer["address"] = object.address
                serializer["phone"] = object.phone
                serializer["params"] = object.params
                serializer["telegram"] = object.telegram
                if object.logo:
                    serializer["logo"] = object.logo.url
                else:
                    serializer["logo"] = None
                serializer["instagram"] = object.instagram
                serializer["facebook"] = object.facebook
                serializer["why_us"] = object.why_us
                serializer["our_history"] = object.our_history
                serializer["program1"] = object.program1
                if object.program1_img:
                    serializer["program1_img"] = object.program1_img.url
                else:
                    serializer["program1_img"] = None
                if object.program2_img:
                    serializer["program2_img"] = object.program2_img.url
                else:
                    serializer["program2_img"] = None
                if object.program3_img:
                    serializer["program3_img"] = object.program3_img.url
                else:
                    serializer["program3_img"] = None
                serializer["program2"] = object.program2
                serializer["program3"] = object.program3
                if object.post_image1:
                    serializer["post_image1"] = object.post_image1.url
                else:
                    serializer["post_image1"] = None
                if object.post_image2:
                    serializer["post_image2"] = object.post_image2.url
                else:
                    serializer["post_image2"] = None
                if object.post_image3:
                    serializer["post_image3"] = object.post_image3.url
                else:
                    serializer["post_image3"] = None
                if object.post_image4:
                    serializer["post_image4"] = object.post_image4.url
                else:
                    serializer["post_image4"] = None
                serializer["post_text1"] = object.post_text1
                serializer["post_text2"] = object.post_text2
                serializer["post_text3"] = object.post_text3
                serializer["post_text4"] = object.post_text4

                return Response(serializer, status=200)
            except Exception as e:
                return Response({'detail': f'{e}',}, status=200)
        return Response(serializer.errors)


class KGINFOView(APIView):
    queryset = KG.objects.all()
    serializer_class = KGInfoS

    def get_object(self, pk):
        try:
            return KG.objects.get(id=pk)
        except Exception as e:
            raise e

    def get(self, request, pk,  format=None):
        # serializer = KGInfoS(data=request.data)
        # if serializer.is_valid():
        #     try:
        # id = serializer.validated_data.get('id')
        id = request.path.split("/")[-1]
        try:
            object = self.get_object(pk)
            rahbariyat = Rahbariyat.objects.filter(kg=object)
            xodim = Xodim.objects.filter(kg=object)
            tadbir = Tadbir.objects.filter(kg=object)
            yangilik = Yangilik.objects.filter(kg=object)
            # post = Post.objects.filter(kg=object)
            oshxona = Oshxona.objects.filter(kg=object)
            menu = []
            for o in oshxona:
                menu += Menu.objects.filter(oshxona=o)
            media = Image_Video.objects.get(kg=object)
            serializer = {
                'rahbariyat': RahbariyatS(rahbariyat, many=True).data,
                'xodim': XodimS(xodim, many=True).data,
                'tadbir': TadbirS(tadbir, many=True).data,
                'yangilik': YangilikS(yangilik, many=True).data,
                # 'post': PostS(post, many=True).data,
                'oshxona': OshxonaSerializer(oshxona, many=True).data,
                'menu': MenuSerializer(menu, many=True).data,
                'media': ImageVideoSerializer(media, many=False).data,
            }
            serializer["id"] = object.id
            serializer["name"] = object.name
            serializer["email"] = object.email
            serializer["viloyat"] = object.viloyat
            serializer["tuman"] = object.tuman
            serializer["number"] = object.number
            serializer["address"] = object.address
            serializer["phone"] = object.phone
            serializer["params"] = object.params
            serializer["telegram"] = object.telegram
            serializer["instagram"] = object.instagram
            serializer["facebook"] = object.facebook
            serializer["why_us"] = object.why_us
            serializer["our_history"] = object.our_history
            serializer["program1"] = object.program1
            serializer["program2"] = object.program2
            serializer["program3"] = object.program3
            if object.program1_img:
                serializer["program1_img"] = object.program1_img.url
            else:
                serializer["program1_img"] = None
            if object.program2_img:
                serializer["program2_img"] = object.program2_img.url
            else:
                serializer["program2_img"] = None
            if object.program3_img:
                serializer["program3_img"] = object.program3_img.url
            else:
                serializer["program3_img"] = None
            if object.post_image1:
                serializer["post_image1"] = object.post_image1.url
            else:
                serializer["post_image1"] = None
            if object.post_image2:
                serializer["post_image2"] = object.post_image2.url
            else:
                serializer["post_image2"] = None
            if object.post_image3:
                serializer["post_image3"] = object.post_image3.url
            else:
                serializer["post_image3"] = None
            if object.post_image4:
                serializer["post_image4"] = object.post_image4.url
            else:
                serializer["post_image4"] = None
            serializer["post_text1"] = object.post_text1
            serializer["post_text2"] = object.post_text2
            serializer["post_text3"] = object.post_text3
            serializer["post_text4"] = object.post_text4
            if object.logo:
                serializer["logo"] = object.logo.url
            else:
                serializer["logo"] = object.logo.url
            return Response(serializer, status=200)
        except Exception as e:
            return Response({'detail': f'{e}',}, status=200)
        return Response(serializer.errors)



class KGUV(RetrieveUpdateDestroyAPIView):
    queryset = KG.objects.all()
    serializer_class = KGS
    allowed_methods = ['HEAD', 'DELETE', 'PATCH']


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

class KitchenCView(ListCreateAPIView):
    queryset = Oshxona.objects.all()
    serializer_class = OshxonaSerializer


class KitchenUView(RetrieveUpdateDestroyAPIView):
    queryset = Oshxona.objects.all()
    serializer_class = OshxonaSerializer

class RahbariyatCV(ListCreateAPIView):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatS


class RahbariyatUV(RetrieveUpdateDestroyAPIView):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatS
    # http_method_names = ['GET', 'PUT', 'PATCH', 'DELETE']

class XodimCV(ListCreateAPIView):
    queryset = Xodim.objects.all()
    serializer_class = XodimS


class XodimUV(RetrieveUpdateDestroyAPIView):
    queryset = Xodim.objects.all()
    serializer_class = XodimS

#
# class PostCV(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostS
#
# class PostUV(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostS

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

class MenuByKGView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs["pk"]
            oshxonalar = Oshxona.objects.filter(kg__id=id)
            menular = []
            for oshxona in oshxonalar:
                menular += Menu.objects.filter(oshxona=oshxona)
            data = {
                'oshxonalar': OshxonaSerializer(oshxonalar, many=True).data,
                'menular': MenuSerializer(menular, many=True).data,
            }
            return Response(data, status=200)
        except Exception as e:
            raise e
class MenuUV(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


from django.utils.http import urlsafe_base64_decode as uid_decoder

class PasswordResetConfirmAPIView(PasswordResetConfirmView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        path = request.path
        uid = path.split('/')[-3]
        uid = force_str(uid_decoder(uid))
        user = User.objects.get(pk=int(float(uid)))
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

from dj_rest_auth.registration.serializers import RegisterSerializer as RS


class RegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = RegisterS

    def post(self, request, *args, **kwargs):
        serializer = RegisterS(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            serializer.save()
            object = VerifyAccountCode.objects.create(email=email)
            object.save()
            subject = 'Tasdiqlash kodi'
            message = f'''
                Assalomu alaykum, Siz bizning saytda ro\'yxatdan o'tdingiz.

                Tasdiqlash kodi: {object.code} .

                Bu kodni hech kimga bermang.

                Xurmat bilan ittower.uz jamoasi.
            '''
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email, ] , fail_silently=False)
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

class VerifyEmail(APIView):
    serializer_class = VerificationCodeS

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data.get('code')
            email = serializer.validated_data.get('email')

            try:
                object = VerifyAccountCode.objects.get(email=email, code=code)
                if object.status == True:
                    message = 'Bu koddan qayta foydalanib bo\'lmaydi.'
                    return Response({'detail': message, }, status=400)
                else:
                    object.status = True
                    object.save()
                    kg = KG.objects.create(email=object.email)
                    kg.save()
                    media = Image_Video.objects.create(kg=kg)
                    media.save()
                return Response({'detail': 'Akkount tasdiqdan o\'tdi.', }, status=201)
            except Exception as e:
                raise e
        return Response(serializer.errors, status=400)


from rest_framework import generics
from django.core.mail import EmailMessage
import random
def get_random_password():
    l=10
    password = ''
    while(l>0):
        p1 = random.choice(list('abcdefghijklmnopqrstuvwxyz'))
        p2 = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        p3 = random.choice(list('0123456789'))
        password += random.choice([p1,p2,p3])
        l -= 1
    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

class VerifyEmailView(generics.GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (AllowAny,)

    def send_gmail(self, email, password):
        message = f'Sizning yangi parolingiz - {password}'
        email = EmailMessage('Sizning yangi parolingiz.', message, to=[email])
        email.send()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                email = serializer.validated_data.get('email')
                key = serializer.validated_data.get('key')
                # email = serializer.validated_data.get('email')

                if email:
                    print(email)
                    try:
                        # id = self.validated_data.get('id')
                        # user = User.objects.get(id=id)
                        user = Token.objects.get(key=key).user
                        user.email = email
                        password = get_random_password()
                        user.set_password(password)
                        user.save()
                        kg, created = KG.objects.get_or_create(email=email)
                        media, created = Image_Video.objects.get_or_create(kg=kg)
                        self.send_gmail(email, password)
                        return Response({"detail": _("ok"), }, status=status.HTTP_200_OK)
                    except Exception as e:
                        # print('error: ', e)
                        # return Response({"detail": _("unauthorized"), }, status=status.HTTP_401_UNAUTHORIZED)
                        raise e
                else:
                    return Response({"detail": _("not found"), }, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response({"detail": " not found",}, status.HTTP_404_NOT_FOUND)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.validated_data

        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })