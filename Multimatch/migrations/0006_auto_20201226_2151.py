# Generated by Django 3.1.4 on 2020-12-26 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Multimatch', '0005_purpose'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='purpose',
            new_name='purposedata',
        ),
    ]