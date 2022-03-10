# Generated by Django 3.2 on 2022-03-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('github_link', models.URLField(blank=True, null=True)),
                ('site_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Previous Projects',
            },
        ),
    ]