# Generated by Django 4.1 on 2022-09-06 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
