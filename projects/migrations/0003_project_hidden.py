# Generated by Django 3.2 on 2022-03-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_previousproject_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
