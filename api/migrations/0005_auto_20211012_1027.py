# Generated by Django 3.1.2 on 2021-10-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211009_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='kg',
            name='post_image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_text1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kg',
            name='post_text4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]