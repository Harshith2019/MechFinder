# Generated by Django 3.1.5 on 2021-05-06 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helps_finished',
            name='is_feedback_given',
        ),
    ]
