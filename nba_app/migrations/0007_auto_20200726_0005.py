# Generated by Django 3.0.8 on 2020-07-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0006_auto_20200726_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
