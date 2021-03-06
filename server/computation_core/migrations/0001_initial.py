# Generated by Django 3.0.6 on 2020-05-15 23:59

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('RE', 'Ready'), ('FA', 'Failed'), ('CO', 'Computing')], default='CO', max_length=2)),
                ('name', models.CharField(max_length=150)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('step', models.FloatField()),
                ('expr_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computation_core.Expression')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', models.FloatField()),
                ('time_ms', models.IntegerField(default=0)),
                ('expr_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computation_core.Expression')),
            ],
        ),
    ]
