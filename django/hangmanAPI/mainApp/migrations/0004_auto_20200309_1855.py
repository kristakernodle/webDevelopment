# Generated by Django 3.0.4 on 2020-03-09 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20200309_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='_solution',
            new_name='solution',
        ),
    ]
