from django.contrib import admin
from .models import *

class KGAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'email', 'phone', 'address', 'telegram',)
    list_filter = ('name', 'email', 'number',)

# class TumanAdmin(admin.ModelAdmin):
#     list_display = ('viloyat', 'name', )
class TadbirAdmin(admin.ModelAdmin):
    list_display = ('kg', 'name', 'text', 'date', 'image', 'address')

class YangilikAdmin(admin.ModelAdmin):
    list_display = ('kg', 'title', 'text', 'date', 'image')

class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ('id', 'kg', 'full_name', 'lavozim', 'mutaxassislik', 'phone','email','telegram', 'image', 'otm', 'date')
    list_filter = ('id', 'kg', 'lavozim', 'mutaxassislik')

class XodimAdmin(admin.ModelAdmin):
    list_display = ('id', 'kg', 'full_name', 'lavozim', 'mutaxassislik','phone', 'email','telegram', 'image', 'otm', 'date')

class Image_VideoAdmin(admin.ModelAdmin):
    list_display = ('kg',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'oshxona', 'name', 'tarkib')
    list_filter = ('id', 'oshxona', 'name')


class VerifyAccountCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'registered_time', 'verified_time', 'status',)

admin.site.register(KG, KGAdmin)
admin.site.register(Tadbir, TadbirAdmin)
admin.site.register(Yangilik, YangilikAdmin)
admin.site.register(Rahbariyat, RahbariyatAdmin)
admin.site.register(Xodim, XodimAdmin)
admin.site.register(Image_Video, Image_VideoAdmin)
admin.site.register(Oshxona)
admin.site.register(Menu, MenuAdmin)

admin.site.register(VerifyAccountCode, VerifyAccountCodeAdmin)
