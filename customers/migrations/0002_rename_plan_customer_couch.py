# Generated by Django 4.0.1 on 2022-02-01 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='plan',
            new_name='couch',
        ),
    ]
