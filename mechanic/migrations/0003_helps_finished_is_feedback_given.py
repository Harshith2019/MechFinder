# Generated by Django 3.1.5 on 2021-05-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic', '0002_remove_helps_finished_is_feedback_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='helps_finished',
            name='is_feedback_given',
            field=models.BooleanField(default=False),
        ),
    ]
