# Generated by Django 5.1 on 2024-08-10 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_profile_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
