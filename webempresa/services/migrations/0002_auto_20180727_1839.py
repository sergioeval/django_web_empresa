# Generated by Django 2.0.2 on 2018-07-27 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='service',
        ),
    ]
