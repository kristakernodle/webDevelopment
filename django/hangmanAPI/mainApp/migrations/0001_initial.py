# Generated by Django 3.0.4 on 2020-03-10 00:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDClass',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('d9057c43-26c4-4f30-a5fe-683f79f40ee7'), editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_solution', models.CharField(max_length=10)),
                ('displayWord', models.CharField(default='__________', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('gameID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.MyUUIDClass')),
            ],
        ),
    ]
