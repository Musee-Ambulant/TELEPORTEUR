# Generated by Django 3.2.6 on 2021-08-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_ami_gif_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='ami',
            name='stl_path',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]