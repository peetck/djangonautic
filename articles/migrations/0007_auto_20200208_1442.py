# Generated by Django 3.0 on 2020-02-08 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='message',
        ),
    ]
