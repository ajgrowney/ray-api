# Generated by Django 3.0.4 on 2020-05-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0002_auto_20200505_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingitem',
            name='remaining_tolerance',
            field=models.IntegerField(default=0),
        ),
    ]