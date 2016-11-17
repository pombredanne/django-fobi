# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-09 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0011_formentry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='formwizardentry',
            name='title',
            field=models.CharField(blank=True, help_text='Shown in templates ifavailable.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='title',
            field=models.CharField(blank=True, help_text='Shown in templates ifavailable.', max_length=255, null=True, verbose_name='Title'),
        ),
    ]
