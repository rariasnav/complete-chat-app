# Generated by Django 5.1.1 on 2024-09-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0004_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='keywords',
            field=models.JSONField(blank=True, null=True),
        ),
    ]