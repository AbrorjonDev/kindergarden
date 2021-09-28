from django.db import models


class Tuman(models.Model):
    VILOYATLAR = (
        ('toshkent', "Toshkent"),
        ('buxoro', 'Buxoro'),
        ('samarqand', 'Samarqand'),
        ('andijon', 'Andijon'),
        ('xorazm', 'Xorazm'),
        ('navoi', 'Navoi'),
    )
    viloyat = models.CharField(choices=VILOYATLAR,max_length=100)
    name = models.CharField(max_length=50)


class KG(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    email = models.EmailField()
    logo = models.ImageField()


class Tadbir(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()
    address = models.CharField(max_length=100)


class Yangilik(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()


class Image_Video(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    image = models.ImageField()


class Rahbariyat(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateTimeField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50)
    about = models.CharField(max_length=50)


class Xodim(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateTimeField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50)
    about = models.CharField(max_length=50)

class Post(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    text = models.TextField()
