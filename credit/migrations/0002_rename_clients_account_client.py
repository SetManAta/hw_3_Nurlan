# Generated by Django 4.1.3 on 2022-12-06 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='clients',
            new_name='client',
        ),
    ]
