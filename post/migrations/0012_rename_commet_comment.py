# Generated by Django 4.2.16 on 2024-09-23 13:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0011_alter_post_author_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]
