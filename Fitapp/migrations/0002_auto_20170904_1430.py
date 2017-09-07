# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hight',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(null=True, verbose_name='Wzrost'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activity',
            field=models.IntegerField(choices=[(0, 'Brak danych'), (1, 'Raczej niska'), (2, 'Umiarkowana aktywność'), (3, 'Aktywny tryb życia'), (4, 'Duża aktywność')], null=True, verbose_name='Aktywność fizyczna'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.DateField(null=True, verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.IntegerField(choices=[(0, 'brak danych'), (1, 'kobieta'), (2, 'mężczyzna')], null=True, verbose_name='Płeć'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(null=True, verbose_name='Waga'),
        ),
    ]
