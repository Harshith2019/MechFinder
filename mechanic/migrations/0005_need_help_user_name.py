# Generated by Django 3.1.5 on 2021-04-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic', '0004_auto_20210405_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='need_help',
            name='user_name',
            field=models.CharField(default='Test Null Value', max_length=200),
            preserve_default=False,
        ),
    ]