# Generated by Django 4.0.1 on 2022-02-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_plan_description_couch_couch_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='month_is_paid',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], max_length=2),
        ),
    ]
