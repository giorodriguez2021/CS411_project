# Generated by Django 3.0.8 on 2020-07-26 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0007_auto_20200726_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='player',
        ),
        migrations.DeleteModel(
            name='PlayerStats',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]