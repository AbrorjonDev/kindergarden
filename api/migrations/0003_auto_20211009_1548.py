# Generated by Django 3.1.2 on 2021-10-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211009_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kg',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='kg',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='telegram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='tuman',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='kg',
            name='viloyat',
            field=models.CharField(blank=True, choices=[('toshkent sh', 'Toshkent shahri'), ('toshkent', 'Toshkent viloyati'), ('buxoro', 'Buxoro viloyati'), ('samarqand', 'Samarqand viloyati'), ('sirdaryo', 'Sirdaryo viloyati'), ('jizzax', 'Jizzax viloyati'), ('qashqadaryo', 'Qashqadaryo'), ('surxondaryo', 'Surxondaryo'), ('qoraqalpoq', "Qoraqalpog'iston Respublikasi"), ('andijon', 'Andijon viloyati'), ('namangan', 'Namangan viloyati'), ("farg'ona", "Farg'ona viloyati"), ('xorazm', 'Xorazm viloyati'), ('navoi', 'Navoiy viloyati')], max_length=40, null=True),
        ),
    ]