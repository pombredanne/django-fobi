# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-05 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0008_formwizardhandlerentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='formwizardentry',
            name='wizard_type',
            field=models.CharField(choices=[(b'SessionWizardView', b'Session wizard'), (b'CookieWizardView', b'Cookie wizard')], default=b'SessionWizardView', help_text='Type of the form wizard.', max_length=255, verbose_name='Type'),
        ),
    ]
