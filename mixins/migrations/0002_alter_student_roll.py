# Generated by Django 4.0.4 on 2022-07-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
        ),
    ]