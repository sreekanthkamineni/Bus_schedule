# Generated by Django 3.2 on 2022-08-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_information',
            name='bus_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Bus_Image/'),
        ),
    ]