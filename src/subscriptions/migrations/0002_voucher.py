# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-06 16:06
from __future__ import unicode_literals

from django.db import migrations, models


def add_voucher_code(apps, schema_editor):
    Voucher = apps.get_model("subscriptions", "Voucher")
    Voucher.objects.create(code='DIAMRING15')


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.RunPython(add_voucher_code),
    ]
