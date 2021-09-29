from django.db import models

#
# class Tuman(models.Model):
#     VILOYATLAR = (
#         ('toshkent', "Toshkent"),
#         ('buxoro', 'Buxoro'),
#         ('samarqand', 'Samarqand'),
#         ('andijon', 'Andijon'),
#         ('xorazm', 'Xorazm'),
#         ('navoi', 'Navoi'),
#     )
#     viloyat = models.CharField(choices=VILOYATLAR, max_length=100)
#     name = models.CharField(max_length=50)
#

class KG(models.Model):

    tuman = models.CharField(max_length=50)
    name = models.CharField(max_length=1000)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    tel = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    email = models.EmailField()
    logo = models.ImageField()

    def __str__(self):
        return self.name

class Tadbir(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField()
    address = models.CharField(max_length=100)

    def __str__(self):
        self.name

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
    video = models.URLField()

    def __str__(self):
        return self.kg


class Rahbariyat(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Xodim(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    date = models.DateField()
    mutaxassislik = models.CharField(max_length=50)
    otm = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Post(models.Model):
    rasm = models.ImageField()
    kg = models.ForeignKey(KG, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.id

class Menu(models.Model):
    kg = models.ForeignKey(KG, on_delete=models.CASCADE, related_name='kindergarden')
    name = models.CharField(max_length=300)
    tarkib = models.TextField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'

    def __str__(self):
        return f'{self.kg.name} - {self.kg.email}'
