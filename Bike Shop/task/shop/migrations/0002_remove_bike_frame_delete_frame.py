# Generated by Django 4.1.1 on 2024-01-26 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='frame',
        ),
        migrations.DeleteModel(
            name='Frame',
        ),
    ]
