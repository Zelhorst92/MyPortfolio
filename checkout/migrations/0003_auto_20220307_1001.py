# Generated by Django 3.2 on 2022-03-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_before_vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
