# Generated by Django 3.1.3 on 2020-11-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHipets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='url',
        ),
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
