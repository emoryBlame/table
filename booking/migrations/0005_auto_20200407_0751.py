# Generated by Django 3.0.5 on 2020-04-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20200406_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
