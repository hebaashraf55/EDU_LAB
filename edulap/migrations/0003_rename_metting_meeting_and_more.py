# Generated by Django 4.2.5 on 2023-10-03 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edulap', '0002_courses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Metting',
            new_name='Meeting',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='mettingName',
            new_name='meetingName',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='mettingPrice',
            new_name='meetingPrice',
        ),
    ]
