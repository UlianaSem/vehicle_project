# Generated by Django 4.2.5 on 2023-10-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_car_owner_moto_owner_alter_milage_moto'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='moto',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]
