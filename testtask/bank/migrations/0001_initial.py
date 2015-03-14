# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.TextField(unique=True, verbose_name='Username', max_length=20)),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=255)),
                ('IDD', models.IntegerField(verbose_name="User's IDD", validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)])),
                ('money_amount', models.DecimalField(decimal_places=2, verbose_name='Amount of your money', max_digits=8)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
