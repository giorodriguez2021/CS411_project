# Generated by Django 3.0.8 on 2020-07-26 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba_app', '0012_auto_20200726_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_number',
            new_name='player_id',
        ),
    ]