from rest_framework import serializers
from .models import *
from rest_framework.response import Response


# class TumanS(serializers.ModelSerializer):
#     class Meta:
#         model = Tuman
#         fields = '__all__'


class KGS(serializers.ModelSerializer):
    class Meta:
        model = KG
        fields = '__all__'


class KGInfoS(serializers.Serializer):
    id = serializers.IntegerField()


class TadbirS(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Tadbir
        fields = '__all__'


class YangilikS(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Yangilik
        fields = "__all__"
    

class RahbariyatS(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Rahbariyat
        fields = '__all__'


class XodimS(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Xodim
        fields = '__all__'



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class ImageVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Video
        fields = '__all__'

class OshxonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Oshxona
        fields = '__all__'

class RegisterS(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        username = self.validated_data.get('username')
        first_name = self.validated_data.get('first_name')
        last_name = self.validated_data.get('last_name')
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')

        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return user

from dj_rest_auth.serializers import ValidationError,force_str, UserModel, PasswordResetConfirmSerializer, PasswordResetSerializer as PasswordSerializer
from django.conf import settings
class CustomPasswordResetSerializer(PasswordSerializer):
    def get_email_options(self):
        return {
            # 'email_template_name': 'registration/password_  reset_email.txt',
            'html_email_template_name': 'password_reset_email.html',
        }
    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'EMAIL_HOST_USER'),
            'request': request,
            ###### USE YOUR TEXT FILE ######
            'email_template_name': 'password_reset_email.html',
        }
        self.reset_form.save(**opts)
from django.contrib.auth.forms import SetPasswordForm

class PasswordResetSerializer(serializers.Serializer):      #serializers.Serializer
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    _errors = {}
    user = None
    set_password_form = None

    def validate(self, attrs):
        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account.forms import default_token_generator
            from allauth.account.utils import url_str_to_user_pk as uid_decoder
        else:
            from django.contrib.auth.tokens import default_token_generator
            from django.utils.http import urlsafe_base64_decode as uid_decoder
            uid = force_str(uid_decoder(attrs['uid']))

        # Decode the uidb64 (allauth use base36) to uid to get User object
        try:
            uid = force_str(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs


    def save(self):
        return self.set_password_form.save()

    def create(self, validated_data):
        return Response(status=201)


class EmailS(serializers.Serializer):
    email = serializers.EmailField(max_length=150)

class VerificationCodeS(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    key = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], "example@gmail.com", validated_data['password'])
        return user

def comparision(new_password1, new_password2):
    if new_password1 == new_password2:
        return True
    return False
from rest_framework.authtoken.models import Token
class PasswordResetS(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=8)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    extra_kwargs = {
        "new_password1":{
            "write_only":True,
        },
        "new_password2":{
            "write_only":True,
        }
    }

    def save(self, attrs):
        try:
            code_obj = VerifyAccountCode.objects.filter(email=attrs["email"]).last()
            code = code_obj.code
            if code == attrs["code"]:
                if attrs["new_password1"] is not None and attrs["new_password1"] is not None:
                    if comparision(new_password1=attrs["new_password1"], new_password2=attrs["new_password2"]):
                        user = User.objects.get(email=attrs["email"])
                        user.set_password(attrs["new_password1"])
                        user.save()
                        code_obj.delete()
                    else:
                        return ValidationError({'detail':['Parol va Parolni tasdiqlash noto\'g\'ri kiritildi.']})
                return ValidationError({"detail": ["Parol maydoni bo\'sh."]})
            else:
                return ValidationError({"detail":["Tasdiqlash kodi noto'g'ri kiritildi."]})

        except Exception as e:
            raise e

    # def validation(self, uid=None, token=None, new_password1=None):# uid, token,
    #
    #     print("uid: {0} ; token: {1}".format(uid, token))
    #     if 'allauth' in settings.INSTALLED_APPS:
    #         from allauth.account.forms import default_token_generator
    #         from allauth.account.utils import url_str_to_user_pk as uid_decoder
    #     else:
    #         from django.contrib.auth.tokens import default_token_generator
    #         from django.utils.http import urlsafe_base64_decode as uid_decoder
    #         uid1 = force_str(uid_decoder(uid))
    #
    #     # Decode the uidb64 (allauth use base36) to uid to get User object
    #     try:
    #         uid1 = force_str(uid_decoder(uid))
    #         print(uid1)
    #         self.user = UserModel._default_manager.get(pk=int(uid1))
    #     # except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
    #     #     raise ValidationError({'uid': ['Invalid value']})
    #     except Exception as e:
    #         print('Exception: ', uid)
    #         raise e
    #     # if not default_token_generator.check_token(self.user, token):
    #     if self.user is not Token.objects.get(key=token).user:
    #         raise ValidationError({'token': ['Invalid value']})
    #
    #     try:
    #         if new_password1 is not None:
    #             self.user.set_password(password=new_password1)
    #         else:
    #             print("parol bo\'sh")
    #     except Exception as e:
    #         raise e
    #
    #     return self.user
    #
    #     # self.custom_validation(attrs)
    #     # # Construct SetPasswordForm instance
    #     # self.set_password_form = self.set_password_form_class(
    #     #     user=self.user, data=attrs,
    #     # )
    #     # if not self.set_password_form.is_valid():
    #     #     raise serializers.ValidationError(self.set_password_form.errors)
    #     #
    #     # return attrs
    #
