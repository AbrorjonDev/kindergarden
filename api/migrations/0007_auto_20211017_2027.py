# Generated by Django 3.1.2 on 2021-10-17 15:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211017_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kg',
            name='params',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), null=True, size=2),
        ),
    ]
