# Generated by Django 4.0.1 on 2022-02-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_plan_customer_couch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couch',
            old_name='plan_description',
            new_name='couch_description',
        ),
        migrations.RenameField(
            model_name='couch',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='couch',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
