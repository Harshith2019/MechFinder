# Generated by Django 3.1.5 on 2021-04-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210406_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='user_name',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]