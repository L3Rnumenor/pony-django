# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OldPerson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lasttname', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('mail', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=5000)),
                ('sexe', models.CharField(choices=[('MEN', 'Men'), ('WOMEN', 'Women')], default='MEN', max_length=10)),
                ('sexualOrientation', models.CharField(choices=[('MEN', 'Men'), ('WOMEN', 'Women'), ('BOTH', 'Both')], default='BOTH', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OldPersonAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elder.Answer')),
                ('oldPerson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elder.OldPerson')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField(max_length=100)),
                ('answerType', models.CharField(choices=[('ONE', 'One answer'), ('MULTIPLE', 'several answers')], default='ONE', max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elder.Question'),
        ),
    ]
