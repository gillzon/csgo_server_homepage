# Generated by Django 3.2.9 on 2022-11-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='steam_id',
            field=models.CharField(blank=True, max_length=40, verbose_name='steam id'),
        ),
    ]