# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import main.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('calories', main.fields.PositiveDecimalField(default=0, max_digits=7, decimal_places=2)),
                ('carbs', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('cholesterol', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('fat', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('fiber', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('protein', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('sodium', main.fields.PositiveDecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('sugar', main.fields.PositiveDecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('servings_per_container', main.fields.PositiveDecimalField(default=1, max_digits=7, decimal_places=2)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 2, 8, 18, 53, 20, 157635, tzinfo=utc), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('notes', models.CharField(max_length=2000, null=True, blank=True)),
                ('servings_consumed', main.fields.PositiveDecimalField(default=0, max_digits=6, decimal_places=2)),
                ('food_consumed', models.ForeignKey(default=0, to='main.Food', unique_for_date=b'date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='food',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
