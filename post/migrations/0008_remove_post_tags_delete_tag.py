# Generated by Django 5.0.6 on 2024-09-21 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_tag_alter_post_options_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
