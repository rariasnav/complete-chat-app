# Generated by Django 5.1.1 on 2024-10-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0014_alter_publishabletoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishabletoken',
            name='token',
            field=models.CharField(default='62ed23b4fa134c62969b2f11ef50d5cd', max_length=255, unique=True),
        ),
    ]
