# Generated by Django 5.1.1 on 2024-10-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0015_alter_publishabletoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishabletoken',
            name='token',
            field=models.CharField(default='e52fe650bf584424942f13a6bc1d7103', max_length=255, unique=True),
        ),
    ]