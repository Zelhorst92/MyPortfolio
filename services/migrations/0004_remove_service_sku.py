# Generated by Django 3.2 on 2022-03-08 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='sku',
        ),
    ]
