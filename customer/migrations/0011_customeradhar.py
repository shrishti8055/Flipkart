# Generated by Django 4.2.1 on 2023-05-26 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAdhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_no', models.IntegerField(blank=True, null=True)),
                ('father_name', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.IntegerField(blank=True, null=True)),
                ('Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
