# Generated by Django 2.1.7 on 2019-05-26 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0024_communitydirectory_communitydirectoryindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communityresource',
            name='description',
        ),
        migrations.RemoveField(
            model_name='communityresource',
            name='resource_type',
        ),
        migrations.RemoveField(
            model_name='communityresource',
            name='website',
        ),
    ]