# Generated by Django 3.0.9 on 2020-08-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games_played',
            field=models.IntegerField(default=0),
        ),
    ]