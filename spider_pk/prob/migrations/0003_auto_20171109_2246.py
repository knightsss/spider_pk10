# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob', '0002_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_range', models.CharField(max_length=100)),
                ('prob_rule', models.CharField(max_length=100)),
                ('prob_match', models.IntegerField()),
                ('prob_nomatch', models.IntegerField()),
                ('prob_bet', models.IntegerField()),
                ('prob_amount', models.IntegerField()),
                ('prob_win', models.FloatField()),
                ('prob_lose', models.FloatField()),
                ('prob_gain', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
    ]
