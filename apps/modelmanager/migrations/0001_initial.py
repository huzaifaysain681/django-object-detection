# Generated by Django 3.2.12 on 2022-08-05 16:15

import django.core.validators
from django.db import migrations, models
import modelmanager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('name', models.CharField(help_text='Name for the machine learning model', max_length=100, verbose_name='Name')),
                ('pth_file', models.FileField(help_text='Allowed extensions are: .pt, .pth', upload_to=modelmanager.models.model_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pt', 'pth'])], verbose_name='Upload Model Pt/Pth File')),
                ('class_filename', models.CharField(help_text='Name for the class file', max_length=100, null=True, verbose_name='Class FileName')),
                ('class_file', models.FileField(help_text='Ml Model classes file. Allowed extensions are: .txt, .names, .yaml', upload_to=modelmanager.models.model_classfile_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'TXT', 'names', 'names', 'yaml', 'YAML'])], verbose_name='Ml Model Classes file')),
                ('description', models.TextField(verbose_name="Model's description")),
                ('version', models.CharField(blank=True, max_length=51, null=True, verbose_name='Ml Model Version')),
                ('public', models.BooleanField(default=False)),
            ],
        ),
    ]
