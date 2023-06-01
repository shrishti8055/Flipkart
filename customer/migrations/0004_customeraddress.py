# Generated by Django 4.2.1 on 2023-05-25 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_dob_alter_customer_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=15, null=True)),
                ('street_no', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('coutry', models.CharField(blank=True, max_length=15, null=True)),
                ('pincode', models.IntegerField(blank=True, max_length=10, null=True)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
