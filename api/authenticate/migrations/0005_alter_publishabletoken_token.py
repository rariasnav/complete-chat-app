# Generated by Django 5.1.1 on 2024-09-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_alter_publishabletoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishabletoken',
            name='token',
            field=models.CharField(default='937127564d6240edaa3ceabb3cb0310b', max_length=255, unique=True),
        ),
    ]