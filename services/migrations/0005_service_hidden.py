# Generated by Django 3.2 on 2022-03-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_service_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
