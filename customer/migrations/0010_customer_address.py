# Generated by Django 4.2.1 on 2023-05-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_remove_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
