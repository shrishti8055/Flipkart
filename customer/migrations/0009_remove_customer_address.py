# Generated by Django 4.2.1 on 2023-05-25 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_rename_coutry_customeraddress_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
    ]
