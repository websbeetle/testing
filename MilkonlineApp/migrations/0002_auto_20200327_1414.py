# Generated by Django 2.2 on 2020-03-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MilkonlineApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
    ]
