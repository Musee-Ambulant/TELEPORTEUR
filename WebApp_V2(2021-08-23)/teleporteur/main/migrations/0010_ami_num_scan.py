# Generated by Django 3.2.6 on 2021-08-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_ami_stl_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='ami',
            name='num_scan',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
