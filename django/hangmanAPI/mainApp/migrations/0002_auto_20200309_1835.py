# Generated by Django 3.0.4 on 2020-03-09 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='getNewWord',
            new_name='Word',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='randomWord',
            new_name='solution',
        ),
    ]
