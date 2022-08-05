# Generated by Django 3.2.12 on 2022-08-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('description', models.TextField()),
                ('inferrenceimage', models.ImageField(blank=True, null=True, upload_to='inferrenceimages')),
                ('detectioninfo', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
