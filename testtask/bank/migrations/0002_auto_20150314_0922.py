# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='money_amount',
            field=models.DecimalField(max_digits=8, verbose_name='Amount of money', decimal_places=2),
            preserve_default=True,
        ),
    ]
