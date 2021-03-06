# Generated by Django 3.0.4 on 2020-05-05 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('parent', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clothingitem',
            name='type',
        ),
        migrations.DeleteModel(
            name='ClothingItemType',
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clothing.ClothingItemCategory'),
        ),
    ]
