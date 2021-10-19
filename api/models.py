from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# User._meta.get_field('username')._unique = False
# User._meta.get_field('username').blank = True
# User._meta.get_field('username').null = False
#
#
# User._meta.get_field('email')._unique = False
# User._meta.get_field('email').blank = False
# User._meta.get_field('email').null = False
# User._meta.get_field('username')._unique = False
# User._meta.get_field('email')._unique = True
# User._meta.get_field('email').blank = False
# User._meta.get_field('email').null = False
#
# class Tuman(models.Model):
VILOYATLAR = (
    ('toshkent sh', 'Toshkent shahri'),
    ('toshkent', "Toshkent viloyati"),
    ('buxoro', 'Buxoro viloyati'),
    ('samarqand', 'Samarqand viloyati'),
    ('sirdaryo', 'Sirdaryo viloyati'),
    ('jizzax', 'Jizzax viloyati'),
    ('qashqadaryo', 'Qashqadaryo'),
    ('surxondaryo', 'Surxondaryo'),
    ('qoraqalpoq', 'Qoraqalpog\'iston Respublikasi'),
    ('andijon', 'Andijon viloyati'),
    ('namangan', 'Namangan viloyati'),
    ('farg\'ona', 'Farg\'ona viloyati'),
    ('xorazm', 'Xorazm viloyati'),
    ('navoi', 'Navoiy viloyati'),
)
#     viloyat = models.CharField(choices=VILOYATLAR, max_length=100)
#     name = models.CharField(max_length=50)
#

class KG(models.Model):
    viloyat = models.CharField(blank=True, null=True,max_length=40)# choices=VILOYATLAR,
    tuman = models.CharField(blank=True, null=True, max_length=50)
    name = models.CharField(blank=True, null=True, max_length=1000)
    number = models.CharField(blank=True, null=True, max_length=20)
    params = ArrayField(
        models.CharField(null=True, blank=True, max_length=50),
        size=2, null=True
    )
    address = models.CharField(blank=True, null=True, max_length=500)
    phone = models.CharField(blank=True, null=True, max_length=50)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to="logo", blank=True, null=True )
    our_history = models.TextField(blank=True, null=True)
    why_us = models.TextField(blank=True, null=True)
    program1 = models.TextField(blank=True, null=True)
    program1_img = models.ImageField(blank=True, null=True, upload_to="program_images")
    program2 = models.TextField(blank=True, null=True)
    program2_img = models.ImageField(blank=True, null=True, upload_to="program_images")
    program3 = models.TextField(blank=True, null=True)
    program3_img = models.ImageField(blank=True, null=True, upload_to="program_images")
    post_image1 = models.ImageField(blank=True, null=True)
    post_text1 = models.TextField(blank=True, null=True)
    post_image2 = models.ImageField(blank=True, null=True)
    post_text2 = models.TextField(blank=True, null=True)
    post_image3 = models.ImageField(blank=True, null=True)
    post_text3 = models.TextField(blank=True, null=True)
    post_image4 = models.ImageField(blank=True, null=True)
    post_text4 = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.email)

    def ImageURL(self):
        if self.post_image4:
            return self.post_image4.url
        else:
            return None

class Tadbir(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Yangilik(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Image_Video(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    image = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()
    image6 = models.ImageField()
    image7 = models.ImageField()
    image8 = models.ImageField()
    # video = models.URLField()

    def __str__(self):
        return self.kg.email



class Rahbariyat(models.Model):
    image = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50)
    about = models.TextField()
    phone = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Xodim(models.Model):
    image = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField()
    phone = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Oshxona(models.Model):
    name = models.CharField(max_length=100)
    kg = models.ForeignKey(KG, on_delete=models.CASCADE, related_name='kindergarden')

    def __str__(self):
        return self.name

class Menu(models.Model):
    oshxona = models.ForeignKey(Oshxona, on_delete=models.CASCADE, related_name='kindergarden')
    name = models.CharField(max_length=300)
    tarkib = models.TextField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'

    def __str__(self):
        return f'{self.name} - {self.oshxona}'

import random
def generate_activation_code():
    code = ''
    for i in range(0, 6):
        code += str(random.randint(0, 10))
    if len(code) == 6:
        print(code)
        return int(code)
    else:
        return generate_activation_code()

def generate_password():
    password = ''
    list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+='
    for i in range(0, 9):
        password += str(random.random(list))
    if len(password) == 6:
        print(password)
        return password
    else:
        return generate_password()

class VerifyAccountCode(models.Model):
    email = models.EmailField(max_length=120)
    code = models.CharField(max_length=6, default=generate_activation_code)
    registered_time = models.DateTimeField(auto_now_add=True)
    verified_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Verify Email Code'
        verbose_name_plural = 'Verify Email Codes'

    def __str__(self):
        return self.email

    # def save(self, request):
    #     if self.verified_time:
    #         self.status = True
    #         return super(VerifyAccountCode, self).save()
