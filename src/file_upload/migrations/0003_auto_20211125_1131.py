# Generated by Django 3.2.9 on 2021-11-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_alter_uploadedfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='result',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
