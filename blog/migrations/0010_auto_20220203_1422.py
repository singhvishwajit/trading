# Generated by Django 3.0.1 on 2022-02-03 08:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20220130_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Investment',
            new_name='Protocol',
        ),
    ]
