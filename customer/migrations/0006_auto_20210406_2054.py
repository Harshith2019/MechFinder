# Generated by Django 3.1.5 on 2021-04-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_helps_received_customer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helps_received',
            name='customer_description',
            field=models.CharField(max_length=1000),
        ),
    ]