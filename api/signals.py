import os.path

from django.db.models.signals import post_delete
from .models import *
from django.dispatch import receiver

def _delete_image(path):
    if os.path.isfile(path):
        os.remove(path)

@receiver(post_delete, sender=Tadbir)
def tadbir_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)


@receiver(post_delete, sender=KG)
def kg_delete(sender, instance, *args, **kwargs):
    if instance.logo:
        _delete_image(instance.logo.path)
    if instance.post_image1:
        _delete_image(instance.post_image1.path)
    if instance.post_image2:
        _delete_image(instance.post_image2.path)
    if instance.post_image2:
        _delete_image(instance.post_image2.path)
    if instance.post_image3:
        _delete_image(instance.post_image3.path)
    if instance.post_image4:
        _delete_image(instance.post_image4.path)
@receiver(post_delete, sender=Yangilik)
def yangilik_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)

@receiver(post_delete, sender=Image_Video)
def tadbir_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)
    if instance.image1:
        _delete_image(instance.image1.path)
    if instance.image2:
        _delete_image(instance.image2.path)
    if instance.image3:
        _delete_image(instance.image3.path)
    if instance.image4:
        _delete_image(instance.image4.path)
    if instance.image5:
        _delete_image(instance.image5.path)
    if instance.image6:
        _delete_image(instance.image6.path)
    if instance.image7:
        _delete_image(instance.image7.path)
    if instance.image8:
        _delete_image(instance.image8.path)
    # if instance.video:
    #     _delete_image(instance.video.path)

@receiver(post_delete, sender=Rahbariyat)
def rahbariyat_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)

@receiver(post_delete, sender=Xodim)
def xodim_delete(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_image(instance.image.path)


