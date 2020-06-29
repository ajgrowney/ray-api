# Generated by Django 3.0.4 on 2020-04-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reminder',
            },
        ),
    ]