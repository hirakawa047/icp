# Generated by Django 4.1.1 on 2022-09-28 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cip', '0002_alter_topic_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='comment',
            new_name='name',
        ),
    ]
