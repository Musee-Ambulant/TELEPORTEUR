# Generated by Django 3.2.6 on 2021-08-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_ami_gif'),
    ]

    operations = [
        migrations.AddField(
            model_name='ami',
            name='gif_path',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]