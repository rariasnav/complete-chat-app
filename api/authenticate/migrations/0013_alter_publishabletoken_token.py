# Generated by Django 5.1.1 on 2024-09-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0012_alter_publishabletoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishabletoken',
            name='token',
            field=models.CharField(default='58f0e2c6bc1c49d5af14870551520da3', max_length=255, unique=True),
        ),
    ]
